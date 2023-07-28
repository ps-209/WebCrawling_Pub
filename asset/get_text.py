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

    def __init__(self, keyword, number, folder,sum_number):
        super(Text,self).__init__()
        multiprocessing.freeze_support()
        self.keyword = keyword
        self.number = number
        self.folder = folder
        self.sum_number = sum_number
        self.power = True

    def internet(self):
        re = requests.get("https://google.com")
        if(re.status_code != 200):
            self.error_occur.emit("lost internet connection")
            return False
        else:
            return True

    def t_crawling(self,url): #newspaper모듈 사용
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

    def get_language(self,title): #제목에서 페이지의 문자 확인
        remove = re.compile(r'[a-zA-Z]')
        if(remove.match(title)):
            return 'en'
        else:
            return 'ko'

    def save_text(self,key_word,contents,count,folder_directory):
        with open(folder_directory + key_word + '.txt','w', encoding='utf-8') as file:
            for i in range(count):
                file.write(str(contents[i]) + '\n')
        
    def get_text(self):
        key_word = self.keyword
        number = int(self.number)
        folder = self.folder
        sum_number = int(self.sum_number)
        
        status = self.internet()
        total_count = 0
        key_word_check = 0 #몇번쨰 키워드인지 구별용
        if(status):
            for key in key_word:
                g_link = 'https://www.google.com/search?q=' + key
                headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'}

                response = requests.get(g_link, headers=headers).text
                soup = BeautifulSoup(response,'html.parser')

                count = 0 #크롤링 페이지 번호
                success = 0
                search_link = '' #링크 확인용
                contents = [] #내용을 담을 리스트
                
                #제목 가져오기
                try:
                    catalog = soup.select('.LC20lb')
                    title = []
                    for i in catalog:
                        title.append(i.get_text())
                except: #가져오는데 실패시 내용을 failed로 저장하고 다음 키워드로 넘어감
                    contents.append("search failed\n")
                    self.progress_updated.emit(key_word_check * number)
                    continue
                #본문 링크 가져오기
                document = soup.select('.yuRUbf')

                #크롤링
                for i in document:
                    if(success == number): #개수가 정해진 숫자에 도달하거나 이전 링크와 동일하다면 패스
                        break
                    elif(i.a.attrs['href'] == search_link):
                        count += 1
                        continue
                    else:
                        search_link = i.a.attrs['href'] #링크 설정
                
                        language = self.get_language(title[count])
                        original_page = self.t_crawling(search_link)
                    
                        if(original_page == '01'):
                            #빈 페이지 또는 크롤링 실패
                            count += 1
                            continue
                        if(language != 'ko' and language != 'en'):
                            count += 1
                            continue

                        pool = multiprocessing.Pool(processes=4)
                        converted_page = pool.apply_async(summarize,args=[language, original_page, 0.85, sum_number])
                        converted_page = str(converted_page.get())
                        pool.close()
                        pool.join()

                        if(converted_page == '001'):
                            #패키지 감지 실패시 경고
                            self.error_occur.emit("package lost")
                            break
                        elif(converted_page == '002'):
                            #벡터화 작업중 실패
                            count += 1
                            continue
                        elif(converted_page == '004'):
                            #페이지 요약 실패시 넘어감
                            count += 1
                            continue

                        contents.append(title[success] + ' : ' + search_link + '\n' + converted_page + '\n')
                        converted_page = None
                        count += 1
                        success += 1
                        total_count += 1
                        self.progress_updated.emit(total_count)
                #크롤링 종료 후 저장
                self.save_text(key,contents,success,folder)
                key_word_check += 1
        del contents
        gc.collect()
        self.process_complete.emit("Crawling Ended","Text Crawling ended\n Total {}".format(total_count))
        self.power = False

    def run(self):
        while(self.power):
            self.get_text()
    
    def stop(self):
        self.power = False
        self.terminate()
        


#ERROR CODE
#01  - crawling error

#004 - error on vectorizing graph