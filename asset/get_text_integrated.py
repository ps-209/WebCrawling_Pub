import requests, re, sys, gc
from bs4 import BeautifulSoup
from newspaper import Article
from asset.summarize_v3 import summarize
from PySide6.QtCore import *
import multiprocessing

class Text(QThread):
    progress_updated = Signal(int)
    error_occur = Signal(str)
    process_complete = Signal(str,str)

    def __init__(self, target, number, folder,sum_number):
        super(Text,self).__init__()
        multiprocessing.freeze_support()
        self.target = target
        self.number = number
        self.folder = folder
        self.sum_number = sum_number
        self.progress_count = 0
        self.power = True

    def internet(self):
        re = requests.get("https://google.com")
        if(re.status_code != 200):
            self.error_occur.emit("lost internet connection")
            return False
        else:
            return True

    def get_crawling(self,url): #newspaper모듈 사용
        try:
            article = Article(url)
            article.download()
            article.parse()
            if(article.text == ''):
                return '01'
            else:
                return article.text
        except:
            return '01'

    def get_language(self,content): #제목에서 페이지의 문자 확인
        korean = re.search(r'[\u3131-\u3163\uac00-\ud7a3]+', content)
        english = re.search(r'[a-zA-Z]+', content)
        if(korean):
            return 'ko'
        elif(english):
            return 'en'
        else:
            return 'unknown'

    def save_text(self,key_word,contents,folder_directory):
        with open(folder_directory + key_word + '.txt','w', encoding='utf-8') as file:
            file.write(str(contents))

    def multiprocess(self,language,content):
        sum_number = int(self.sum_number)
        pool = multiprocessing.Pool(processes=2)
        converted_page = pool.apply_async(summarize,args=[language, content, 0.85, sum_number])
        converted = str(converted_page.get())
        pool.close()
        pool.join()
        return converted

    def keyword_crawling(self,keyword):
        number  = int(self.number) #키워드 당 구해야하는 개수
        link = "https://www.google.com/search?q=" + str(keyword) #구글 검색
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'}

        response = requests.get(link,headers=headers).text
        soup = BeautifulSoup(response,'html.parser')

        count = int(0) #제목과 내용 연동을 위한 카운트
        keyword_count = int(0) #키워드 성공 개수, number일치 확인
        prev_link = ''
        final_content = []

        catalog = soup.select('.LC20lb')
        if(catalog == ''):
            self.save_text(keyword,"Crawling Failed",self.folder) #save text = str저장으로 변환
            self.progress_count += number
            self.progress_updated.emit(self.progress_count)
            return
        else:
            title = []
            for i in catalog:
                title.append(i.get_text())
        
        link_collect = soup.select('.yuRUbf')
        for i in link_collect:
            curr_link = i.a.attrs['href']
            if(keyword_count == number):
                break
            elif(prev_link == curr_link):
                #이전 링크와 현재 링크가 일치 -> 패스
                count += 1
                continue

            content = self.get_crawling(curr_link)
            if(content == '01'):
                count += 1
                continue
            else:
                language = self.get_language(title[count])
            
            if(language == "unknown"):
                count += 1
                continue
            else: #multiprocess로 분리
                tem_content = self.multiprocess(language,content)
                if(tem_content == '002'):
                    count += 1
                    continue
                elif(tem_content == "004"):
                    count += 1
                    continue
                else:
                    final_content.append(title[count] + ' : ' + curr_link + '\n' + tem_content + '\n')
                    self.progress_count += 1
                    self.progress_updated.emit(self.progress_count)
                    keyword_count += 1
                    count += 1

        summarized_content = '\n'.join(final_content)
        self.save_text(keyword,summarized_content,self.folder)
    
    def site_crawling(self,site):
        content = self.get_crawling(site)
        if(content == '01'):
            summarized_content = "Site Crawling Failed..."
        else:
            language = self.get_language(content)

            if(language == 'unknown'):
                content = "Failed to check language"
            else:
                summarized_content = self.multiprocess(language,content)
                if(summarized_content == '002'):
                    summarized_content = "Failed to Vectorize Text"
                elif(summarized_content == "004"):
                    summarized_content = "Failed to Summarize Text"
        
        summarized_content = site + '\n' + summarized_content
        self.save_text(f"site_crawling_{self.progress_count}",summarized_content,self.folder)
        self.progress_count += 1
        self.progress_updated.emit(self.progress_count)

    def switching(self):
        target = self.target #리스트 형태로 존재
        if(self.internet == False):
            return
        for i in target:
            if("http" in i or "html" in i):
                self.site_crawling(i)
            else:
                self.keyword_crawling(i)
        gc.collect()
        self.process_complete.emit("completed","Text Crawling Ended")
        self.power = False

    def run(self):
        while(self.power):
            self.switching()
    
    def stop(self):
        self.power = False
        self.quit()
        self.wait(3000)