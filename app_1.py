import sys, asyncio
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import *
from t1_dev_ui import Ui_MainWindow
from get_image import Img
from crawling_dev_v2 import Txt
from threading import Thread

class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_window,self).__init__()
        self.setupUi(self)
        self.search_button.clicked.connect(self.directory)
        self.photo_button.clicked.connect(self.image)
        self.text_button.clicked.connect(self.text)

    def SD(self): #버튼 비활성화
        self.search_button.setDisabled(True)
        self.text_button.setDisabled(True)
        self.photo_button.setDisabled(True)
        self.keyword_edit.setDisabled(True)
        self.directory_edit.setDisabled(True)

    def SE(self): #버튼 활성화
        self.search_button.setEnabled(True)
        self.text_button.setEnabled(True)
        self.photo_button.setEnabled(True)
        self.keyword_edit.setEnabled(True)
        self.directory_edit.setEnabled(True)
    
    def directory(self): #경로 설정
        direct = QFileDialog.getExistingDirectory(self)
        self.directory_edit.setText(direct)
        if(not direct):
            return

        MBox = QMessageBox(self)
        MBox.setWindowTitle("Information")
        MBox.setText("Directory is confirmed")
        MBox.setIcon(QMessageBox.Information)
        button1 = MBox.exec()
        
    def image(self): #이미지
        self.SD()
        thread = Thread(target=self.img_search)
        thread.start()

    def img_search(self):
        keyword = self.keyword_edit.text()
        directory = self.directory_edit.text() + '/'
        if(not directory or not keyword):
            self.AlartBox()
            self.SE()
            return
        
        count = int(self.comboBox.currentText())
        try:
            Img(keyword,count,directory)
        except:
            print('error-1')
        self.SE()

    def text(self): #텍스트
        self.SD()
        thread = Thread(target=self.txt_search)
        thread.start()
    
    def txt_search(self):
        keyword = self.keyword_edit.text()
        directory = self.directory_edit.text() + '/'
        if(not directory or not keyword):
            self.AlartBox()
            self.SE()
            return
        
        count = int(self.comboBox.currentText())
        try:
            Txt(keyword,count,directory)
        except:
            print('error-2')
        self.SE()

    def AlartBox(self):
        alartbox = QMessageBox(self)
        alartbox.setWindowTitle("ERROR")
        alartbox.setText("Please fill empty parts!")
        alartbox.setIcon(QMessageBox.Warning)
        button1 = alartbox.exec()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Main_window()
    window.show()

    app.exec()

#새로운 스레드에서 함수를 시작하지 않으면 함수가 끝날 때까지 GUI가 멈추기 때문에
#thread 사용으로 새로운 함수를 시작하도록 함