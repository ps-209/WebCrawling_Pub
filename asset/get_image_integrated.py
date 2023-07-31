from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time, requests
import os, logging, bs4
from PySide6.QtCore import *

class Image(QThread):
    progress_updated = Signal(int)
    error_occur = Signal(str)
    process_complete = Signal(str,str)

    def __init__(self, target,number,folder,picture_type):
        super(Image,self).__init__()
        self.target = target
        self.number = number
        self.folder = folder
        self.picture_type = picture_type
        self.progress_count = int(0)
        self.power = True

    def switching(self):
        target = self.target
        if(self.get_internet == False):
            self.power = False
            return
        for i in target:
            if("http" in i or "html" in i):
                self.site_image(i)
            else:
                self.keyword_image(i)

        self.process_complete.emit("Download Ended",
        "Image Crawling ended\n Total {} downloaded".format(self.progress_count))
        self.power = False

    def run(self): #메인
        while(self.power):
            self.switching()
            break

    def stop(self):
        self.power = False
        self.quit()
        self.wait(3000)

    def site_image(self,site):
        response = requests.get(site)
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        img_num = int(0)
        for tag in soup.find_all('img'):
            src = tag.get('src')
            if(src):
                self.download("Site-Image",src,img_num) #이미지 최소 용량 설정 -> 쓸데없는 이미지 다운 방지?
                img_num += 1

        self.progress_count += 1
        self.progress_updated.emit(self.progress_count)

    def keyword_image(self,keyword):
        max = int(self.number)
        #브라우저 설정
        bw_options = webdriver.ChromeOptions()

        bw_options.add_argument('--headless')
        #user-agent는 구글에 user agent string 검색후 자신의 브라우저 에이젼트 복사해 사용
        bw_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43")
        bw_options.add_argument('--disable-gpu')
        bw_options.add_argument('--mute-audio')
        bw_options.add_argument('--disable-extensions')
        bw_options.add_argument('--remote-allow-origins=*')
        #작동 테스트시 추가
        #bw_options.add_experimental_option('detach', True)
        
        #브라우저 + WDM로그 제거
        os.environ['WDM_PROGRESS_BAR'] = str(0)
        os.environ['WDM_LOG'] = str(logging.NOTSET)
        serv = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=serv,options=bw_options)

        #검색
        browser.get("https://www.google.com/search?q=" + keyword + "&source=lnms&tbm=isch")
        browser.implicitly_wait(3)
        browser.execute_script('window.scrollTo(0,0);')

        img_num = int(0) #이미지 넘버링
        i = int(1) #이미지 순서를 위한
        while(True):
            if(img_num == max):
                break
            if(i % 25 == 0): #매 25번째 이미지는 온전한 이미지 형태가 아니라서 건너뜀
                i += 1
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
                    confirm = self.download(keyword,ImageURL,img_num)
                    if(confirm):
                        self.progress_count += 1
                        img_num += 1
                        self.progress_updated.emit(self.progress_count)
                        break
                    else:
                        break
                else:
                    CurrentTime = time.time()
                    if(CurrentTime - StartTime > 7):
                        break
            i += 1

    def download(self,keyword,url,num):
        directory = self.folder
        picture_type = str(self.picture_type)
        try:
            re = requests.get(url)
            if(re.status_code == 200):
                with open(directory + keyword + '-' + str(num) + '.' + picture_type, 'wb') as file:
                    file.write(re.content)
            else:
                return False
        except:
            return False
        else:
            return True
        
    def get_internet(self):
        re = requests.get("https://google.com")
        if(re.status_code != 200):
            self.error_occur.emit("lost internet connection")
            return False
        else:
            return True
