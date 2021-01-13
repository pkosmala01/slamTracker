# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stats_window.ui'
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
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.category = QLabel(self.centralwidget)
        self.category.setObjectName(u"category")

        self.horizontalLayout.addWidget(self.category)

        self.player_1_name = QLabel(self.centralwidget)
        self.player_1_name.setObjectName(u"player_1_name")

        self.horizontalLayout.addWidget(self.player_1_name)

        self.player_2_name = QLabel(self.centralwidget)
        self.player_2_name.setObjectName(u"player_2_name")

        self.horizontalLayout.addWidget(self.player_2_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.category_2 = QLabel(self.centralwidget)
        self.category_2.setObjectName(u"category_2")

        self.horizontalLayout_2.addWidget(self.category_2)

        self.player_1_nationality = QLabel(self.centralwidget)
        self.player_1_nationality.setObjectName(u"player_1_nationality")

        self.horizontalLayout_2.addWidget(self.player_1_nationality)

        self.player_2_nationality = QLabel(self.centralwidget)
        self.player_2_nationality.setObjectName(u"player_2_nationality")

        self.horizontalLayout_2.addWidget(self.player_2_nationality)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.category_3 = QLabel(self.centralwidget)
        self.category_3.setObjectName(u"category_3")

        self.horizontalLayout_3.addWidget(self.category_3)

        self.player_1_first_match = QLabel(self.centralwidget)
        self.player_1_first_match.setObjectName(u"player_1_first_match")

        self.horizontalLayout_3.addWidget(self.player_1_first_match)

        self.player_2_first_match = QLabel(self.centralwidget)
        self.player_2_first_match.setObjectName(u"player_2_first_match")

        self.horizontalLayout_3.addWidget(self.player_2_first_match)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.category_4 = QLabel(self.centralwidget)
        self.category_4.setObjectName(u"category_4")

        self.horizontalLayout_4.addWidget(self.category_4)

        self.player_1_matches_played = QLabel(self.centralwidget)
        self.player_1_matches_played.setObjectName(u"player_1_matches_played")

        self.horizontalLayout_4.addWidget(self.player_1_matches_played)

        self.player_2_matches_played = QLabel(self.centralwidget)
        self.player_2_matches_played.setObjectName(u"player_2_matches_played")

        self.horizontalLayout_4.addWidget(self.player_2_matches_played)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.category_5 = QLabel(self.centralwidget)
        self.category_5.setObjectName(u"category_5")

        self.horizontalLayout_5.addWidget(self.category_5)

        self.player_1_matches_won = QLabel(self.centralwidget)
        self.player_1_matches_won.setObjectName(u"player_1_matches_won")

        self.horizontalLayout_5.addWidget(self.player_1_matches_won)

        self.player_2_matches_won = QLabel(self.centralwidget)
        self.player_2_matches_won.setObjectName(u"player_2_matches_won")

        self.horizontalLayout_5.addWidget(self.player_2_matches_won)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.category_6 = QLabel(self.centralwidget)
        self.category_6.setObjectName(u"category_6")

        self.horizontalLayout_6.addWidget(self.category_6)

        self.player_1_same_surface_played = QLabel(self.centralwidget)
        self.player_1_same_surface_played.setObjectName(u"player_1_same_surface_played")

        self.horizontalLayout_6.addWidget(self.player_1_same_surface_played)

        self.player_2_same_surface_played = QLabel(self.centralwidget)
        self.player_2_same_surface_played.setObjectName(u"player_2_same_surface_played")

        self.horizontalLayout_6.addWidget(self.player_2_same_surface_played)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.category_7 = QLabel(self.centralwidget)
        self.category_7.setObjectName(u"category_7")

        self.horizontalLayout_7.addWidget(self.category_7)

        self.player_1_same_surface_won = QLabel(self.centralwidget)
        self.player_1_same_surface_won.setObjectName(u"player_1_same_surface_won")

        self.horizontalLayout_7.addWidget(self.player_1_same_surface_won)

        self.player_2_same_surface_won = QLabel(self.centralwidget)
        self.player_2_same_surface_won.setObjectName(u"player_2_same_surface_won")

        self.horizontalLayout_7.addWidget(self.player_2_same_surface_won)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.category_8 = QLabel(self.centralwidget)
        self.category_8.setObjectName(u"category_8")

        self.horizontalLayout_8.addWidget(self.category_8)

        self.player_1_best_finish = QLabel(self.centralwidget)
        self.player_1_best_finish.setObjectName(u"player_1_best_finish")

        self.horizontalLayout_8.addWidget(self.player_1_best_finish)

        self.player_2_best_finish = QLabel(self.centralwidget)
        self.player_2_best_finish.setObjectName(u"player_2_best_finish")

        self.horizontalLayout_8.addWidget(self.player_2_best_finish)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.category_9 = QLabel(self.centralwidget)
        self.category_9.setObjectName(u"category_9")

        self.horizontalLayout_9.addWidget(self.category_9)

        self.player_1_best_finish_tournament = QLabel(self.centralwidget)
        self.player_1_best_finish_tournament.setObjectName(u"player_1_best_finish_tournament")

        self.horizontalLayout_9.addWidget(self.player_1_best_finish_tournament)

        self.player_2_best_finish_tournament = QLabel(self.centralwidget)
        self.player_2_best_finish_tournament.setObjectName(u"player_2_best_finish_tournament")

        self.horizontalLayout_9.addWidget(self.player_2_best_finish_tournament)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.category_10 = QLabel(self.centralwidget)
        self.category_10.setObjectName(u"category_10")

        self.horizontalLayout_10.addWidget(self.category_10)

        self.player_1_best_finish_grand_slam = QLabel(self.centralwidget)
        self.player_1_best_finish_grand_slam.setObjectName(u"player_1_best_finish_grand_slam")

        self.horizontalLayout_10.addWidget(self.player_1_best_finish_grand_slam)

        self.player_2_best_finish_grand_slam = QLabel(self.centralwidget)
        self.player_2_best_finish_grand_slam.setObjectName(u"player_2_best_finish_grand_slam")

        self.horizontalLayout_10.addWidget(self.player_2_best_finish_grand_slam)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.category_11 = QLabel(self.centralwidget)
        self.category_11.setObjectName(u"category_11")

        self.horizontalLayout_11.addWidget(self.category_11)

        self.player_1_titles = QLabel(self.centralwidget)
        self.player_1_titles.setObjectName(u"player_1_titles")

        self.horizontalLayout_11.addWidget(self.player_1_titles)

        self.player_2_titles = QLabel(self.centralwidget)
        self.player_2_titles.setObjectName(u"player_2_titles")

        self.horizontalLayout_11.addWidget(self.player_2_titles)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionOd_poczatku)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOd_poczatku.setText(QCoreApplication.translate("MainWindow", u"Od pocz\u0105tku", None))
        self.category.setText(QCoreApplication.translate("MainWindow", u"Imi\u0119 i nazwisko", None))
        self.player_1_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.category_2.setText(QCoreApplication.translate("MainWindow", u"Narodowo\u015b\u0107", None))
        self.player_1_nationality.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_nationality.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.category_3.setText(QCoreApplication.translate("MainWindow", u"Pocz\u0105tek kariery", None))
        self.player_1_first_match.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_first_match.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.category_4.setText(QCoreApplication.translate("MainWindow", u"Mecze rozegrane", None))
        self.player_1_matches_played.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_matches_played.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.category_5.setText(QCoreApplication.translate("MainWindow", u"Mecze wygrane", None))
        self.player_1_matches_won.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_matches_won.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.category_6.setText(QCoreApplication.translate("MainWindow", u"Mecze rozegrane na nawierzchni turnieju", None))
        self.player_1_same_surface_played.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_same_surface_played.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.category_7.setText(QCoreApplication.translate("MainWindow", u"Mecze wygrane na nawierzchni turnieju", None))
        self.player_1_same_surface_won.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_same_surface_won.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.category_8.setText(QCoreApplication.translate("MainWindow", u"Najwy\u017csze miejsce", None))
        self.player_1_best_finish.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_best_finish.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.category_9.setText(QCoreApplication.translate("MainWindow", u"Najwy\u017csze miejsce w poprzednich edycjach turnieju", None))
        self.player_1_best_finish_tournament.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_best_finish_tournament.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.category_10.setText(QCoreApplication.translate("MainWindow", u"Najwy\u017csze miejsce w turnieju wielkoszlemowym", None))
        self.player_1_best_finish_grand_slam.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_best_finish_grand_slam.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.category_11.setText(QCoreApplication.translate("MainWindow", u"Liczba tytu\u0142\u00f3w", None))
        self.player_1_titles.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_titles.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

