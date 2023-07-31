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
        MainWindow.setMaximumSize(QSize(800, 800))
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
        self.progressBar.setValue(0)
        self.add_list = QPushButton(self.centralwidget)
        self.add_list.setObjectName(u"add_list")
        self.add_list.setGeometry(QRect(470, 40, 51, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 240, 35, 35))
        self.label_3.setPixmap(QPixmap(u":/icon/icon/file_icon.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 280, 91, 31))
        self.add_opt = QComboBox(self.centralwidget)
        self.add_opt.addItem("")
        self.add_opt.addItem("")
        self.add_opt.addItem("")
        self.add_opt.addItem("")
        self.add_opt.setObjectName(u"add_opt")
        self.add_opt.setGeometry(QRect(449, 280, 71, 31))
        self.add_opt.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 280, 51, 31))
        self.option_select = QComboBox(self.centralwidget)
        self.option_select.addItem("")
        self.option_select.addItem("")
        self.option_select.setObjectName(u"option_select")
        self.option_select.setGeometry(QRect(250, 280, 81, 31))
        self.option_select.setFont(font)
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

        self.add_opt.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WebCrawling", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">KeyWord</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Amount</span></p></body></html>", None))
        self.amout_number.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.amout_number.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.amout_number.setItemText(2, QCoreApplication.translate("MainWindow", u"5", None))
        self.amout_number.setItemText(3, QCoreApplication.translate("MainWindow", u"7", None))
        self.amout_number.setItemText(4, QCoreApplication.translate("MainWindow", u"9", None))

        self.add_list.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Summarize</span></p></body></html>", None))
        self.add_opt.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.add_opt.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.add_opt.setItemText(2, QCoreApplication.translate("MainWindow", u"5", None))
        self.add_opt.setItemText(3, QCoreApplication.translate("MainWindow", u"7", None))

        self.add_opt.setCurrentText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Option</span></p></body></html>", None))
        self.option_select.setItemText(0, QCoreApplication.translate("MainWindow", u"Text", None))
        self.option_select.setItemText(1, QCoreApplication.translate("MainWindow", u"Picture", None))

        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"KeyList", None));
    # retranslateUi

