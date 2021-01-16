# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOd_poczatku = QAction(MainWindow)
        self.actionOd_poczatku.setObjectName(u"actionOd_poczatku")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.listWidget_2 = QListWidget(self.centralwidget)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_2.addWidget(self.listWidget_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.lineEdit)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout.addWidget(self.listWidget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_3.addWidget(self.lineEdit_3)

        self.listWidget_3 = QListWidget(self.centralwidget)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.verticalLayout_3.addWidget(self.listWidget_3)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        self.NextButton = QPushButton(self.centralwidget)
        self.NextButton.setObjectName(u"NextButton")
        self.NextButton.setEnabled(False)

        self.gridLayout.addWidget(self.NextButton, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit, self.listWidget)
        QWidget.setTabOrder(self.listWidget, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.listWidget_2)
        QWidget.setTabOrder(self.listWidget_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.listWidget_3)
        QWidget.setTabOrder(self.listWidget_3, self.NextButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Slam Tracker", None))
        self.actionOd_poczatku.setText(QCoreApplication.translate("MainWindow", u"Od pocz\u0105tku", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Zawodnik 2", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wpisz nazwisko...", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Zawodnik 1", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wpisz nazwisko...", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Turniej", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Wpisz nazw\u0119/miasto", None))
        self.NextButton.setText(QCoreApplication.translate("MainWindow", u"Dalej", None))
    # retranslateUi

