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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)
import asset.resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(532, 402)
        MainWindow.setMaximumSize(QSize(532, 402))
        font = QFont()
        font.setPointSize(10)
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/icon/w.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.search_button = QPushButton(self.centralwidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(470, 240, 51, 31))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.search_button.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 71, 21))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.label_2.setFont(font2)
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(10, 280, 71, 31))
        self.label_1.setFont(font1)
        self.amout_number = QComboBox(self.centralwidget)
        self.amout_number.addItem("")
        self.amout_number.addItem("")
        self.amout_number.addItem("")
        self.amout_number.addItem("")
        self.amout_number.addItem("")
        self.amout_number.setObjectName(u"amout_number")
        self.amout_number.setGeometry(QRect(90, 280, 69, 31))
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
        self.progressBar.setFont(font1)
        self.progressBar.setValue(0)
        self.add_list = QPushButton(self.centralwidget)
        self.add_list.setObjectName(u"add_list")
        self.add_list.setGeometry(QRect(470, 40, 51, 31))
        self.add_list.setFont(font2)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 240, 35, 35))
        self.label_3.setPixmap(QPixmap(u":/icon/icon/file_icon.png"))
        self.label_3.setScaledContents(True)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(350, 280, 91, 31))
        self.label_5.setFont(font1)
        self.add_opt = QComboBox(self.centralwidget)
        self.add_opt.addItem("")
        self.add_opt.addItem("")
        self.add_opt.addItem("")
        self.add_opt.addItem("")
        self.add_opt.setObjectName(u"add_opt")
        self.add_opt.setGeometry(QRect(449, 280, 71, 31))
        self.add_opt.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 280, 51, 31))
        self.label_4.setFont(font1)
        self.option_select = QComboBox(self.centralwidget)
        self.option_select.addItem("")
        self.option_select.addItem("")
        self.option_select.setObjectName(u"option_select")
        self.option_select.setGeometry(QRect(250, 280, 81, 31))
        self.option_select.setFont(font1)
        self.start_button = QPushButton(self.centralwidget)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(10, 320, 511, 41))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.start_button.setFont(font3)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 80, 511, 151))
        font5 = QFont()
        font5.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.tableWidget.setFont(font5)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(36)
        self.version = QLabel(self.centralwidget)
        self.version.setObjectName(u"version")
        self.version.setGeometry(QRect(470, 10, 48, 16))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(11)
        font6.setStyleStrategy(QFont.PreferAntialias)
        self.version.setFont(font6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.add_opt.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WebCrawling", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">KeyWord</span></p></body></html>", None))
        self.label_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Amount</span></p></body></html>", None))
        self.amout_number.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.amout_number.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.amout_number.setItemText(2, QCoreApplication.translate("MainWindow", u"5", None))
        self.amout_number.setItemText(3, QCoreApplication.translate("MainWindow", u"7", None))
        self.amout_number.setItemText(4, QCoreApplication.translate("MainWindow", u"9", None))

        self.add_list.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Summarize</span></p></body></html>", None))
        self.add_opt.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.add_opt.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.add_opt.setItemText(2, QCoreApplication.translate("MainWindow", u"5", None))
        self.add_opt.setItemText(3, QCoreApplication.translate("MainWindow", u"7", None))

        self.add_opt.setCurrentText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Option</span></p></body></html>", None))
        self.option_select.setItemText(0, QCoreApplication.translate("MainWindow", u"Text", None))
        self.option_select.setItemText(1, QCoreApplication.translate("MainWindow", u"Picture", None))

        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"KeyList", None));
        self.version.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">v1.0.0</p></body></html>", None))
    # retranslateUi

