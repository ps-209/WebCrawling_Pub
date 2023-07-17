import requests, re
from PySide6.QtCore import *
from asset.summarize_v3 import summarize
from newspaper import Article

class Web_Text(QThread):
    progress_updated = Signal(int)
    error_occur = Signal(str)
    process_complete = Signal(str,str)

    def __init__(self, sites, folder):
        super().__init__()
        self.sites = sites
        self.folder = folder

    def internet(self):
        re = requests.get("https://google.com")
        if(re.status_code != 200):
            self.error_occur.emit("lost internet connection")
            return 1
        else:
            return 200
        
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

    def language_detection(self,text):
        korean = re.search(r'[\u3131-\u3163\uac00-\ud7a3]+', text)
        english = re.search(r'[a-zA-Z]+', text)
        
        if(korean):
            return 'ko'
        elif(english):
            return 'en'
        else:
            return 'unknown'
        
    def save_text(self,contents,count,folder_directory):
        with open(folder_directory + 'site_crawling.txt','w', encoding='utf-8') as file:
            for i in range(count):
                file.write(str(contents[i]) + '\n')
        self.process_complete.emit("Crawling Ended","Web Text Crawling ended\n Total {}".format(count))

    def run(self):
        sites = self.sites
        folder = self.folder

        num = 0
        collection = []
        status = self.internet()
        if(status == 200):
            for i in sites:
                contents = self.crawling(i)
                if(contents == '01'):#실패 처리
                    collection.append(i + '\nCrawling Failed\n')
                else:
                    language = self.language_detection(contents)
                    if(language == 'unknown'):
                        collection.append(i + '\nPage Language Error\n')
                    else:
                        summarized = summarize(language,contents,0.85,5)
                        if(summarized == '001'):
                            self.error_occur.emit("package lost")
                            collection.append(i + '\nFailed By Package Lost\n')
                        elif(summarized == '002'):
                            collection.append(i + '\nFailed to Vectorize text\n')
                        elif(summarized == '004'):
                            collection.append(i + '\nFailed to summarize\n')
                        else:
                            collection.append(i + '\n' + summarized + '\n')
                num += 1
                self.progress_updated.emit(num)
            self.save_text(collection,num,folder)
        
        self.quit()
        self.wait(3000)

    
