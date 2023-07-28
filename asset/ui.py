# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 't1_dev.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)
import asset.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(531, 401)
        MainWindow.setMaximumSize(QSize(529, 400))
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/icon/app_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.search_button = QPushButton(self.centralwidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(470, 240, 51, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 71, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 280, 71, 31))
        self.amout_number = QComboBox(self.centralwidget)
        self.amout_number.addItem("")
        self.amout_number.addItem("")
        self.amout_number.addItem("")
        self.amout_number.addItem("")
        self.amout_number.addItem("")
        self.amout_number.setObjectName(u"amout_number")
        self.amout_number.setGeometry(QRect(80, 280, 69, 31))
        self.amout_number.setFont(font)
        self.directory_edit = QLineEdit(self.centralwidget)
        self.directory_edit.setObjectName(u"directory_edit")
        self.directory_edit.setGeometry(QRect(50, 240, 411, 31))
        self.directory_edit.setFont(font)
        self.keyword_edit = QLineEdit(self.centralwidget)
        self.keyword_edit.setObjectName(u"keyword_edit")
        self.keyword_edit.setGeometry(QRect(10, 40, 451, 31))
        self.keyword_edit.setFont(font)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 370, 511, 23))
        self.progressBar.setValue(0)
        self.add_list = QPushButton(self.centralwidget)
        self.add_list.setObjectName(u"add_list")
        self.add_list.setGeometry(QRect(470, 40, 51, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 240, 35, 35))
        self.label_3.setPixmap(QPixmap(u":/icon/icon/file_icon.png"))
        self.label_3.setScaledContents(True)
        self.sum_check = QCheckBox(self.centralwidget)
        self.sum_check.setObjectName(u"sum_check")
        self.sum_check.setGeometry(QRect(340, 280, 16, 31))
        self.sum_check.setChecked(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 280, 81, 31))
        self.sum_number = QComboBox(self.centralwidget)
        self.sum_number.addItem("")
        self.sum_number.addItem("")
        self.sum_number.addItem("")
        self.sum_number.setObjectName(u"sum_number")
        self.sum_number.setGeometry(QRect(451, 280, 69, 31))
        self.sum_number.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(190, 280, 51, 31))
        self.picture_type = QComboBox(self.centralwidget)
        self.picture_type.addItem("")
        self.picture_type.addItem("")
        self.picture_type.setObjectName(u"picture_type")
        self.picture_type.setGeometry(QRect(250, 280, 69, 31))
        self.picture_type.setFont(font)
        self.pic_check = QCheckBox(self.centralwidget)
        self.pic_check.setObjectName(u"pic_check")
        self.pic_check.setGeometry(QRect(170, 287, 16, 20))
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(10, 320, 511, 41))
        font1 = QFont()
        font1.setPointSize(11)
        self.start_button.setFont(font1)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 80, 511, 151))
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(36)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.sum_number.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WebCrawling", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">KeyWord</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Amount</span></p></body></html>", None))
        self.amout_number.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.amout_number.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.amout_number.setItemText(2, QCoreApplication.translate("MainWindow", u"5", None))
        self.amout_number.setItemText(3, QCoreApplication.translate("MainWindow", u"7", None))
        self.amout_number.setItemText(4, QCoreApplication.translate("MainWindow", u"9", None))

        self.add_list.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_3.setText("")
        self.sum_check.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Summarize</span></p></body></html>", None))
        self.sum_number.setItemText(0, QCoreApplication.translate("MainWindow", u"3", None))
        self.sum_number.setItemText(1, QCoreApplication.translate("MainWindow", u"5", None))
        self.sum_number.setItemText(2, QCoreApplication.translate("MainWindow", u"7", None))

        self.sum_number.setCurrentText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Picture</span></p></body></html>", None))
        self.picture_type.setItemText(0, QCoreApplication.translate("MainWindow", u"png", None))
        self.picture_type.setItemText(1, QCoreApplication.translate("MainWindow", u"jpg", None))

        self.pic_check.setText("")
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"KeyList", None));
    # retranslateUi

