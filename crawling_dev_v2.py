from typing import Optional
import requests, re, os
from bs4 import BeautifulSoup
from newspaper import Article
from summarize_v2 import summarize_sentence
from PySide6.QtCore import *

class Text(QThread):
    progress_updated = Signal(int)
    error_occur = Signal(str)

    def __init__(self, keyword, number, folder):
        super().__init__()
        self.keyword = keyword
        self.number = number
        self.folder = folder

    def internet(self):
        re = requests.get("https://google.com")
        if(re.status_code != 200):
            self.error_occur.emit("lost internet connection")
            return 1
        else:
            return 200

    def t_crawling(self,link): #링크 설정시 페이지 전체 내용 크롤링
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'}
        t_page = requests.get(link, headers=headers).text
        t_soup = BeautifulSoup(t_page, 'html.parser')
        try:
            text = t_soup.get_text()
            return text
        except:
            return '01'

    def t2_crawling(self,url,language): #newspaper모듈 사용
        try:
            article = Article(url,language)
            article.download()
            article.parse()
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
        self.error_occur.emit("success")
        #print("success")

    def run(self):
        key_word = str(self.keyword)
        number = int(self.number)
        folder = self.folder
        status = self.internet()
        if(status == 200):

            g_link = 'https://www.google.com/search?q=' + key_word
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'}

            response = requests.get(g_link, headers=headers).text
            soup = BeautifulSoup(response,'html.parser')

            #제목 가져오기
            catalog = soup.select('.LC20lb')
            title = []
            for i in catalog:
                title.append(i.get_text())

            #본문 링크 가져오기
            document = soup.select('.yuRUbf')

            count = 0 #크롤링할 페이지 수 세기
            search_link = '' #링크 확인용
            contents = [] #내용을 담을 리스트

            #크롤링
            for i in document:
                if(count == number): #개수가 정해진 숫자에 도달하거나 이전 링크와 동일하다면 패스
                    break
                elif(i.a.attrs['href'] == search_link):
                    continue
                else:
                    search_link = i.a.attrs['href'] #링크 설정
            
                    language = self.get_language(title[count])
                    original_page = self.t2_crawling(search_link,language)
                
                    if(original_page == '01'):
                        print('crawling error. skip this page')
                        continue
                    if(language != 'ko' and language != 'en'):
                        continue

                    converted_page = summarize_sentence(language, original_page, 0.85, 5)

                    if(len(converted_page) <= 5):
                        print('error on summarization. Code : ' + converted_page)
                        continue

                    contents.append(title[count] + ' : ' + search_link + '\n' + converted_page)
                    count += 1
                    self.progress_updated.emit(count)

            self.save_text(key_word,contents,count,folder)

        self.quit()
        self.wait()

    
# word = str(input('Search for : '))
# number = int(input('How many : '))
#searching(word,number,directory)


#ERROR CODE
#01  - crawling error

#004 - error on vectorizing graph