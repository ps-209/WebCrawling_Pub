import sys, asyncio
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import *
from t1_dev_ui import Ui_MainWindow
from get_image import Image
from crawling_dev_v2 import Text
from threading import Thread

class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_window,self).__init__()
        self.work_thread = None
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
        MBox.exec()
        
    def image(self): #이미지
        self.SD()
        thread = Thread(target=self.img_search(self))
        thread.start()
        #여기서 self는 메인윈도우의 스레드 코드를 가지고 있으므로 넘겨줘야 창이 뜸

    def img_search(self,main):
        keyword = self.keyword_edit.text()
        directory = self.directory_edit.text() + '/'
        if(not directory or not keyword):
            main.AlartBox("Please fill empty parts!")
            self.SE()
            return
        
        count = int(self.comboBox.currentText())
        self.progressBar.setMaximum(count)
        try:
            self.work_thread = Image(keyword,count,directory)
            self.work_thread.progress_updated.connect(self.update_progress)
            self.work_thread.error_occur.connect(self.error)
            self.work_thread.finished.connect(self.SE)
            self.work_thread.start()
        except:
            print('error-1')
            return
 

    def text(self): #텍스트
        self.SD()
        thread = Thread(target=self.txt_search(self))
        thread.start()
    
    def txt_search(self,main):
        keyword = self.keyword_edit.text()
        directory = self.directory_edit.text() + '/'
        if(not directory or not keyword):
            main.AlartBox("Please fill empty parts!")
            self.SE()
            return
        
        count = int(self.comboBox.currentText())
        self.progressBar.setMaximum(count)
        try:
            self.work_thread = Text(keyword,count,directory)
            self.work_thread.progress_updated.connect(self.update_progress)
            self.work_thread.error_occur.connect(self.error)
            self.work_thread.finished.connect(self.SE)
            self.work_thread.start()
        except:
            print('error-2')
            return

    def update_progress(self,value):
        self.progressBar.setValue(value)

    def error(self,content):
        self.AlartBox(content)

    def closeEvent(self,event):
        if(self.work_thread and self.work_thread.isRunning()):
            self.work_thread.quit()
            self.work_thread.wait()
        event.accept()

    def AlartBox(self,content):
        alartbox = QMessageBox(self)
        alartbox.setWindowTitle("ERROR")
        alartbox.setText(content)
        alartbox.setIcon(QMessageBox.Warning)
        alartbox.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Main_window()
    window.show()

    app.exec()

#새로운 스레드에서 함수를 시작하지 않으면 함수가 끝날 때까지 GUI가 멈추기 때문에
#thread 사용으로 새로운 함수를 시작하도록 함