from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time, requests
import os, logging
from PySide6.QtCore import *

class Image(QThread):
    progress_updated = Signal(int)
    error_occur = Signal(str)
    process_complete = Signal(str,str)

    def __init__(self, keyword,number,folder):
        super(Image,self).__init__()
        self.keyword = keyword
        self.number = number
        self.folder = folder

    def run(self): #메인
        max = self.number

        self.image_search()
        
        self.quit()
        self.wait(3000)
    
    def internet(self):
        re = requests.get("https://google.com")
        if(re.status_code != 200):
            self.error_occur.emit("lost internet connection")
            return 1
        else:
            return 200
        #인터넷 연결 검증후 - 정상 : 200, 비정상 1 반환

    def image_search(self):
        keyword = self.keyword
        max = self.number
        folder_directory = self.folder
        failed = int(0)

        status = self.internet()
        if(status == 200):

            #브라우저 설정
            #bw_options = Options()
            bw_options = webdriver.ChromeOptions()

            bw_options.add_argument('--headless')
            #user-agent는 구글에 user agent string 검색후 자신의 브라우저 에이젼트 복사해 사용
            bw_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43")
            bw_options.add_argument('--disable-gpu')
            bw_options.add_argument('--mute-audio')
            bw_options.add_argument('--disable-extensions')
            bw_options.add_argument('--remote-allow-origins=*')
            
            #브라우저
            #bw_options.add_experimental_option('detach', True)
            os.environ['WDM_PROGRESS_BAR'] = str(0)
            os.environ['WDM_LOG'] = str(logging.NOTSET)
            serv = Service(ChromeDriverManager().install())
            browser = webdriver.Chrome(service=serv,options=bw_options)

            #검색
            browser.get("https://www.google.com/search?q=" + keyword + "&source=lnms&tbm=isch")
            browser.implicitly_wait(3)
            browser.execute_script('window.scrollTo(0,0);')

            for i in range(1,max+1):
                if(i % 25 == 0): #매 25번째 이미지는 온전한 이미지 형태가 아니라서 건너뜀
                    continue
                xPath = '//*[@id="islrg"]/div[1]/div[%s]'%i

                #미리보기 이미지 경로
                PreviewXPath = '//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img'%i
                Preview = browser.find_element(By.XPATH,PreviewXPath)
                PreviewURL = Preview.get_attribute('src')

                #이미지 클릭
                browser.find_element(By.XPATH,xPath).click()

                #미리보기 이미지, 클릭된 이미지 대조 확인
                StartTime = time.time()
                while True:
                    Image = browser.find_element(By.XPATH,'//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]')
                    ImageURL = Image.get_attribute('src')

                    

                    if(ImageURL != PreviewURL):
                        break
                    else:
                        CurrentTime = time.time()
                        if(CurrentTime - StartTime > 7):
                            #print("Pass {} for time out".format(i))
                            break
                

                #이미지 다운로드 시도
                try:
                    re = requests.get(ImageURL)
                    if(re.status_code == 200):
                        with open(folder_directory + keyword + '-' + str(i) + '.jpg', 'wb') as file:
                            file.write(re.content)
                except:
                    failed += 1
                else:
                    self.progress_updated.emit(i)

            self.process_complete.emit("Download Ended","Image Crawling ended\n Total {} downloaded".format(max - failed))
