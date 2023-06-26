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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(491, 202)
        MainWindow.setMaximumSize(QSize(491, 231))
        icon = QIcon()
        icon.addFile(u":/newPrefix/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.search_button = QPushButton(self.centralwidget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(434, 30, 51, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 65, 181, 21))
        self.text_button = QPushButton(self.centralwidget)
        self.text_button.setObjectName(u"text_button")
        self.text_button.setGeometry(QRect(330, 90, 71, 71))
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icon/text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.text_button.setIcon(icon1)
        self.text_button.setIconSize(QSize(50, 50))
        self.photo_button = QPushButton(self.centralwidget)
        self.photo_button.setObjectName(u"photo_button")
        self.photo_button.setGeometry(QRect(410, 90, 71, 71))
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icon/photo.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.photo_button.setIcon(icon2)
        self.photo_button.setIconSize(QSize(50, 50))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 5, 381, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 130, 71, 31))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(250, 130, 69, 31))
        self.directory_edit = QLineEdit(self.centralwidget)
        self.directory_edit.setObjectName(u"directory_edit")
        self.directory_edit.setGeometry(QRect(10, 30, 421, 31))
        self.keyword_edit = QLineEdit(self.centralwidget)
        self.keyword_edit.setObjectName(u"keyword_edit")
        self.keyword_edit.setGeometry(QRect(10, 90, 311, 31))
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 170, 471, 23))
        self.progressBar.setValue(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WebCrawling", None))
        self.search_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">KeyWord</span></p></body></html>", None))
        self.text_button.setText("")
        self.photo_button.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">File Directory</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Amount</span></p></body></html>", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"9", None))

    # retranslateUi

