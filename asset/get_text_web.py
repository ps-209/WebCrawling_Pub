import requests, re, gc, bs4
from PySide6.QtCore import *
from asset.summarize_v3 import summarize
from newspaper import Article
import multiprocessing


class Web_Text(QThread):
    progress_updated = Signal(int)
    error_occur = Signal(str)
    process_complete = Signal(str,str)

    def __init__(self, sites, folder,sum_number):
        super(Web_Text,self).__init__()
        multiprocessing.freeze_support()
        self.sites = sites
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
        
    def crawling(self,site):
        try:
            article = Article(site)
            article.download()
            article.parse()
            if(article.text == ''):
                return '01'
            else:
                return article.text
        except:
            return '01'
        # try:
        #     response = requests.get(site)
        #     soup = bs4.BeautifulSoup(response.content,'html.parser')
        #     text_list = soup.find_all(text=True)
        #     text = ''
        #     if(text_list == '' or len(text_list) == 0):
        #         return '01'
        #     for i in text_list:
        #         text + str(i)
        #     return text
        # except:
        #     return '01'

    def language_detection(self,text):
        korean = re.search(r'[\u3131-\u3163\uac00-\ud7a3]+', text)
        english = re.search(r'[a-zA-Z]+', text)
        
        if(korean):
            return 'ko'
        elif(english):
            return 'en'
        else:
            return 'unknown'
        
    def save_text(self,count,folder_directory):
        global collection
        with open(folder_directory + 'site_crawling.txt','w', encoding='utf-8') as file:
            for i in range(count):
                file.write(str(collection[i]) + '\n')

    def get_web(self):
        sites = self.sites
        folder = self.folder
        sum_number = int(self.sum_number)

        num = 0
        global collection
        collection = []
        status = self.internet()
        if(status):
            for i in sites:
                contents = self.crawling(i)
                if(contents == '01'):#실패 처리
                    collection.append(i + '\nCrawling Failed\n')
                else:
                    language = self.language_detection(contents)
                    if(language == 'unknown'):
                        collection.append(i + '\nPage Language Error\n')
                    else:
                        
                        pool = multiprocessing.Pool(processes=2)
                        converted_page = pool.apply_async(summarize,args=[language, contents, 0.85, sum_number])
                        converted_page = str(converted_page.get())
                        pool.close()
                        pool.join()

                        #summarized = summarize(language,contents,0.85,sum_number)
                        if(converted_page == '001'):
                            self.error_occur.emit("package lost")
                            collection.append(i + '\nFailed By Package Lost\n')
                        elif(converted_page == '002'):
                            collection.append(i + '\nFailed to Vectorize text\n')
                        elif(converted_page == '004'):
                            collection.append(i + '\nFailed to summarize\n')
                        else:
                            collection.append(i + '\n' + converted_page + '\n')
                num += 1
                self.progress_updated.emit(num)
            self.save_text(num,folder)
        self.power = False
        del collection
        gc.collect()
        self.process_complete.emit("Crawling Ended","Web Text Crawling ended\n Total {}".format(num))
        

    def run(self):
        while(self.power):
            self.get_web()
    
    def stop(self):
        self.power = False
        self.quit()
        self.wait(3000)

