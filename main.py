import sys,gc
from PySide6.QtWidgets import *
from PySide6.QtCore import *

from multiprocessing import freeze_support
from asset.ui import Ui_MainWindow
from threading import Thread
#사용자 파일
from asset.get_image_integrated import Image
from asset.get_text_integrated import Text
class Main_window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Main_window,self).__init__()
        self.setFixedSize(529, 400)
        self.work_thread = None
        self.setupUi(self)
        self.tableWidget.setColumnWidth(0,self.tableWidget.width())
        self.search_button.clicked.connect(self.directory)
        self.add_list.clicked.connect(self.adding_list)
        self.start_button.clicked.connect(self.service_start)

    def SD(self): #버튼 비활성화
        self.search_button.setDisabled(True)
        self.keyword_edit.setDisabled(True)
        self.directory_edit.setDisabled(True)
        self.amout_number.setDisabled(True)
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
        self.amout_number.setEnabled(True)
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
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1,int(0),QTableWidgetItem(content))
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

    def img_search(self,target):
        directory = self.directory_edit.text() + '/'
        picture_type = self.picture_type.currentText()
        count = int(self.amout_number.currentText())
        total = int(0)
        for i in target:
            if("http" in i or "html" in i):
                total += 1
            else:
                total += count
        self.progressBar.setMaximum(total)
        self.progressBar.setValue(0)
        try:
            self.work_thread = Image(target,count,directory,picture_type)
            self.work_thread.progress_updated.connect(self.update_progress)
            self.work_thread.error_occur.connect(self.error)
            self.work_thread.process_complete.connect(self.ending)
            self.work_thread.finished.connect(self.SE)
            self.work_thread.start()
        except:
            self.error("Error on Searching Image")
            self.SE()
            return
    
    def txt_search_integrated(self,target):
        directory = self.directory_edit.text() + '/'
        count = int(self.amout_number.currentText())
        sum_number = self.sum_number.currentText()
        total = 0
        for i in target:
            if("http" in i or "html" in i):
                total += 1
            else:
                total += count
        self.progressBar.setMaximum(total)
        self.progressBar.setValue(0)
        try:
            self.work_thread = Text(target,count,directory,sum_number)
            self.work_thread.progress_updated.connect(self.update_progress)
            self.work_thread.error_occur.connect(self.error)
            self.work_thread.process_complete.connect(self.ending)
            self.work_thread.finished.connect(self.SE)
            self.work_thread.start()
        except:
            self.error("Error on Searching Text")
            return

    def service_start(self):
        self.SD()
        content_list = []
        
        for i in range(self.tableWidget.rowCount()):
            tem_content = self.tableWidget.item(i,0).text()
            if(tem_content):
                content_list.append(tem_content)
            else:
                pass
        if(self.blank_check(content_list)):
            self.SE()
            self.AlartBox("fill empty parts")
            return
        if(self.sum_check.isChecked() == True and self.pic_check.isChecked() == True):
            self.AlartBox("Please check one")
            self.SE()
        elif(self.sum_check.isChecked() == True):
            thread = Thread(target=self.txt_search_integrated(content_list))
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
        self.tableWidget.setRowCount(0)
        gc.collect()
        
        
    def closeEvent(self,event):
        if(self.work_thread and self.work_thread.isRunning()):
            try:
                self.work_thread.stop()
            except:
                pass
        event.accept()

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
    freeze_support()
    app = QApplication(sys.argv)
    
    window = Main_window()
    window.show()
    sys.exit(app.exec())

#새로운 스레드에서 함수를 시작하지 않으면 함수가 끝날 때까지 GUI가 멈추기 때문에
#thread 사용으로 새로운 함수를 시작하도록 함