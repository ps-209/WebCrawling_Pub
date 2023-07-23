import sys,gc
from PySide6.QtWidgets import *
from asset.ui import Ui_MainWindow
from threading import Thread
#사용자 파일
from asset.get_image import Image
from asset.get_text import Text
from asset.get_text_web import Web_Text

class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_window,self).__init__()
        self.setFixedSize(529, 400)
        self.work_thread = None
        self.setupUi(self)
        self.show()
        self.search_button.clicked.connect(self.directory)
        self.add_list.clicked.connect(self.adding_list)
        self.start_button.clicked.connect(self.service_start)

    def SD(self): #버튼 비활성화
        self.search_button.setDisabled(True)
        self.keyword_edit.setDisabled(True)
        self.directory_edit.setDisabled(True)
        self.comboBox.setDisabled(True)
        self.add_list.setDisabled(True)
        self.start_button.setDisabled(True)
        self.pic_check.setDisabled(True)
        self.sum_check.setDisabled(True)
        self.picture_type.setDisabled(True)
        self.sum_number.setDisabled(True)

    def SE(self): #버튼 활성화
        self.search_button.setEnabled(True)
        self.keyword_edit.setEnabled(True)
        self.directory_edit.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.add_list.setEnabled(True)
        self.start_button.setEnabled(True)
        self.pic_check.setEnabled(True)
        self.sum_check.setEnabled(True)
        self.picture_type.setEnabled(True)
        self.sum_number.setEnabled(True)

    def adding_list(self):
        content = self.keyword_edit.text()
        if(content == ''):
            return
        else:
            self.listWidget.addItem(str(content))
            self.keyword_edit.setText("")
    
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

    def img_search(self,key_list):
        directory = self.directory_edit.text() + '/'
        picture_type = self.picture_type.currentText()
        count = int(self.comboBox.currentText())
        self.progressBar.setMaximum(count * len(key_list))
        self.progressBar.setValue(0)
        try:
            self.work_thread = Image(key_list,count,directory,picture_type)
            self.work_thread.progress_updated.connect(self.update_progress)
            self.work_thread.error_occur.connect(self.error)
            self.work_thread.process_complete.connect(self.ending)
            self.work_thread.finished.connect(self.SE)
            self.work_thread.start()
        except:
            self.error("Error on Searching Image")
            self.SE()
            return
    
    def txt_search_keyword(self,key_list):
        directory = self.directory_edit.text() + '/'
        count = int(self.comboBox.currentText())
        sum_number = self.sum_number.currentText()
        self.progressBar.setMaximum(count * len(key_list))
        self.progressBar.setValue(0)
        try:
            self.work_thread = Text(key_list,count,directory,sum_number)
            self.work_thread.progress_updated.connect(self.update_progress)
            self.work_thread.error_occur.connect(self.error)
            self.work_thread.process_complete.connect(self.ending)
            self.work_thread.finished.connect(self.SE)
            self.work_thread.start()
        except:
            self.error("Error on Searching Text")
            return
        
    def txt_search_web(self,url_list):
        directory = self.directory_edit.text() + '/'
        sum_number = self.sum_number.currentText()
        self.progressBar.setMaximum(len(url_list))
        self.progressBar.setValue(0)
        try:
            self.work_thread = Web_Text(url_list,directory,sum_number)
            self.work_thread.progress_updated.connect(self.update_progress)
            self.work_thread.error_occur.connect(self.error)
            self.work_thread.process_complete.connect(self.ending)
            self.work_thread.finished.connect(self.SE)
            self.work_thread.start()
        except:
            self.error("Error on Crawling Text")
            return
        
    def service_start(self):
        self.SD()
        count = self.listWidget.count()
        content_list = []
        
        for i in range(count):
            content_list.append(self.listWidget.item(i).text())
        if(self.blank_check(content_list)):
            self.SE()
            self.error("fill empty parts")
            return
        if(self.sum_check.isChecked() == True and self.pic_check.isChecked() == True):
            self.error("Please check one")
            self.SE()
        elif(self.sum_check.isChecked() == True):
            if("http" in content_list[0] or "html" in content_list[0]):
                thread = Thread(target=self.txt_search_web(content_list))
                thread.start()
            else:
                thread = Thread(target=self.txt_search_keyword(content_list))
                thread.start()
        elif(self.pic_check.isChecked() == True):
            thread = Thread(target=self.img_search(content_list))
            thread.start()

    def blank_check(self,content):
        directory = self.directory_edit.text()
        if(directory == '' or content == ''):
            return True
        else:
            return False

    def update_progress(self,value):
        self.progressBar.setValue(value)

    def error(self,content):
        self.AlartBox(content)

    def ending(self,title,content):
        self.work_thread.stop()
        self.CompleteBox(title,content)
        self.listWidget.clear()
        gc.collect()
        
    def closeEvent(self,event):
        gc.collect()
        if(self.work_thread and self.work_thread.isRunning()):
            self.work_thread.stop()
        event.accept()
        QApplication.quit()

    def AlartBox(self,content):
        alartbox = QMessageBox(self)
        alartbox.setWindowTitle("Warning")
        alartbox.setText(content)
        alartbox.setIcon(QMessageBox.Critical)
        alartbox.exec()

    def CompleteBox(self,title,content):
        combox = QMessageBox(self)
        combox.setWindowTitle(title)
        combox.setText(content)
        combox.setIcon(QMessageBox.Information)
        combox.exec()

if __name__ == '__main__':
    app = QApplication()

    window = Main_window()

    sys.exit(app.exec())

#새로운 스레드에서 함수를 시작하지 않으면 함수가 끝날 때까지 GUI가 멈추기 때문에
#thread 사용으로 새로운 함수를 시작하도록 함