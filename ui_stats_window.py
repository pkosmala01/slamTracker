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

from PySide2.QtCharts import QtCharts


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionOd_poczatku = QAction(MainWindow)
        self.actionOd_poczatku.setObjectName(u"actionOd_poczatku")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 761, 541))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.category = QLabel(self.layoutWidget)
        self.category.setObjectName(u"category")

        self.verticalLayout.addWidget(self.category)

        self.category_2 = QLabel(self.layoutWidget)
        self.category_2.setObjectName(u"category_2")

        self.verticalLayout.addWidget(self.category_2)

        self.category_3 = QLabel(self.layoutWidget)
        self.category_3.setObjectName(u"category_3")

        self.verticalLayout.addWidget(self.category_3)

        self.category_4 = QLabel(self.layoutWidget)
        self.category_4.setObjectName(u"category_4")

        self.verticalLayout.addWidget(self.category_4)

        self.category_5 = QLabel(self.layoutWidget)
        self.category_5.setObjectName(u"category_5")

        self.verticalLayout.addWidget(self.category_5)

        self.category_6 = QLabel(self.layoutWidget)
        self.category_6.setObjectName(u"category_6")

        self.verticalLayout.addWidget(self.category_6)

        self.category_7 = QLabel(self.layoutWidget)
        self.category_7.setObjectName(u"category_7")

        self.verticalLayout.addWidget(self.category_7)

        self.category_8 = QLabel(self.layoutWidget)
        self.category_8.setObjectName(u"category_8")

        self.verticalLayout.addWidget(self.category_8)

        self.category_9 = QLabel(self.layoutWidget)
        self.category_9.setObjectName(u"category_9")

        self.verticalLayout.addWidget(self.category_9)

        self.category_10 = QLabel(self.layoutWidget)
        self.category_10.setObjectName(u"category_10")

        self.verticalLayout.addWidget(self.category_10)

        self.category_11 = QLabel(self.layoutWidget)
        self.category_11.setObjectName(u"category_11")

        self.verticalLayout.addWidget(self.category_11)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(7)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.player_1_name = QLabel(self.layoutWidget)
        self.player_1_name.setObjectName(u"player_1_name")
        self.player_1_name.setFrameShape(QFrame.NoFrame)
        self.player_1_name.setAlignment(Qt.AlignCenter)
        self.player_1_name.setMargin(0)
        self.player_1_name.setIndent(1)

        self.verticalLayout_2.addWidget(self.player_1_name)

        self.player_1_nationality = QLabel(self.layoutWidget)
        self.player_1_nationality.setObjectName(u"player_1_nationality")
        self.player_1_nationality.setFrameShape(QFrame.NoFrame)
        self.player_1_nationality.setAlignment(Qt.AlignCenter)
        self.player_1_nationality.setMargin(0)
        self.player_1_nationality.setIndent(1)

        self.verticalLayout_2.addWidget(self.player_1_nationality)

        self.player_1_first_match = QLabel(self.layoutWidget)
        self.player_1_first_match.setObjectName(u"player_1_first_match")
        self.player_1_first_match.setFrameShape(QFrame.NoFrame)
        self.player_1_first_match.setAlignment(Qt.AlignCenter)
        self.player_1_first_match.setMargin(0)
        self.player_1_first_match.setIndent(1)

        self.verticalLayout_2.addWidget(self.player_1_first_match)

        self.player_1_matches_played = QLabel(self.layoutWidget)
        self.player_1_matches_played.setObjectName(u"player_1_matches_played")
        self.player_1_matches_played.setFrameShape(QFrame.NoFrame)
        self.player_1_matches_played.setAlignment(Qt.AlignCenter)
        self.player_1_matches_played.setMargin(0)
        self.player_1_matches_played.setIndent(1)

        self.verticalLayout_2.addWidget(self.player_1_matches_played)

        self.player_1_matches_won = QLabel(self.layoutWidget)
        self.player_1_matches_won.setObjectName(u"player_1_matches_won")
        self.player_1_matches_won.setFrameShape(QFrame.NoFrame)
        self.player_1_matches_won.setAlignment(Qt.AlignCenter)
        self.player_1_matches_won.setMargin(0)
        self.player_1_matches_won.setIndent(1)

        self.verticalLayout_2.addWidget(self.player_1_matches_won)

        self.player_1_same_surface_played = QLabel(self.layoutWidget)
        self.player_1_same_surface_played.setObjectName(u"player_1_same_surface_played")
        self.player_1_same_surface_played.setFrameShape(QFrame.NoFrame)
        self.player_1_same_surface_played.setAlignment(Qt.AlignCenter)
        self.player_1_same_surface_played.setMargin(0)
        self.player_1_same_surface_played.setIndent(1)

        self.verticalLayout_2.addWidget(self.player_1_same_surface_played)

        self.player_1_same_surface_won = QLabel(self.layoutWidget)
        self.player_1_same_surface_won.setObjectName(u"player_1_same_surface_won")
        self.player_1_same_surface_won.setFrameShape(QFrame.NoFrame)
        self.player_1_same_surface_won.setAlignment(Qt.AlignCenter)
        self.player_1_same_surface_won.setMargin(0)
        self.player_1_same_surface_won.setIndent(1)

        self.verticalLayout_2.addWidget(self.player_1_same_surface_won)

        self.player_1_best_finish = QLabel(self.layoutWidget)
        self.player_1_best_finish.setObjectName(u"player_1_best_finish")
        self.player_1_best_finish.setFrameShape(QFrame.NoFrame)
        self.player_1_best_finish.setAlignment(Qt.AlignCenter)
        self.player_1_best_finish.setMargin(0)
        self.player_1_best_finish.setIndent(1)

        self.verticalLayout_2.addWidget(self.player_1_best_finish)

        self.player_1_best_finish_tournament = QLabel(self.layoutWidget)
        self.player_1_best_finish_tournament.setObjectName(u"player_1_best_finish_tournament")
        self.player_1_best_finish_tournament.setFrameShape(QFrame.NoFrame)
        self.player_1_best_finish_tournament.setAlignment(Qt.AlignCenter)
        self.player_1_best_finish_tournament.setMargin(0)
        self.player_1_best_finish_tournament.setIndent(1)

        self.verticalLayout_2.addWidget(self.player_1_best_finish_tournament)

        self.player_1_best_finish_grand_slam = QLabel(self.layoutWidget)
        self.player_1_best_finish_grand_slam.setObjectName(u"player_1_best_finish_grand_slam")
        self.player_1_best_finish_grand_slam.setFrameShape(QFrame.NoFrame)
        self.player_1_best_finish_grand_slam.setAlignment(Qt.AlignCenter)
        self.player_1_best_finish_grand_slam.setMargin(0)
        self.player_1_best_finish_grand_slam.setIndent(1)

        self.verticalLayout_2.addWidget(self.player_1_best_finish_grand_slam)

        self.player_1_titles = QLabel(self.layoutWidget)
        self.player_1_titles.setObjectName(u"player_1_titles")
        self.player_1_titles.setFrameShape(QFrame.NoFrame)
        self.player_1_titles.setAlignment(Qt.AlignCenter)
        self.player_1_titles.setMargin(0)
        self.player_1_titles.setIndent(1)

        self.verticalLayout_2.addWidget(self.player_1_titles)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.player_2_name = QLabel(self.layoutWidget)
        self.player_2_name.setObjectName(u"player_2_name")
        self.player_2_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.player_2_name)

        self.player_2_nationality = QLabel(self.layoutWidget)
        self.player_2_nationality.setObjectName(u"player_2_nationality")
        self.player_2_nationality.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.player_2_nationality)

        self.player_2_first_match = QLabel(self.layoutWidget)
        self.player_2_first_match.setObjectName(u"player_2_first_match")
        self.player_2_first_match.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.player_2_first_match)

        self.player_2_matches_played = QLabel(self.layoutWidget)
        self.player_2_matches_played.setObjectName(u"player_2_matches_played")
        self.player_2_matches_played.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.player_2_matches_played)

        self.player_2_matches_won = QLabel(self.layoutWidget)
        self.player_2_matches_won.setObjectName(u"player_2_matches_won")
        self.player_2_matches_won.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.player_2_matches_won)

        self.player_2_same_surface_played = QLabel(self.layoutWidget)
        self.player_2_same_surface_played.setObjectName(u"player_2_same_surface_played")
        self.player_2_same_surface_played.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.player_2_same_surface_played)

        self.player_2_same_surface_won = QLabel(self.layoutWidget)
        self.player_2_same_surface_won.setObjectName(u"player_2_same_surface_won")
        self.player_2_same_surface_won.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.player_2_same_surface_won)

        self.player_2_best_finish = QLabel(self.layoutWidget)
        self.player_2_best_finish.setObjectName(u"player_2_best_finish")
        self.player_2_best_finish.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.player_2_best_finish)

        self.player_2_best_finish_tournament = QLabel(self.layoutWidget)
        self.player_2_best_finish_tournament.setObjectName(u"player_2_best_finish_tournament")
        self.player_2_best_finish_tournament.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.player_2_best_finish_tournament)

        self.player_2_best_finish_grand_slam = QLabel(self.layoutWidget)
        self.player_2_best_finish_grand_slam.setObjectName(u"player_2_best_finish_grand_slam")
        self.player_2_best_finish_grand_slam.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.player_2_best_finish_grand_slam)

        self.player_2_titles = QLabel(self.layoutWidget)
        self.player_2_titles.setObjectName(u"player_2_titles")
        self.player_2_titles.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.player_2_titles)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.chartView = QtCharts.QChartView(self.layoutWidget)
        self.chartView.setObjectName(u"chartView")

        self.horizontalLayout_2.addWidget(self.chartView)

        self.chartView_2 = QtCharts.QChartView(self.layoutWidget)
        self.chartView_2.setObjectName(u"chartView_2")

        self.horizontalLayout_2.addWidget(self.chartView_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_4.setStretch(0, 100)
        self.verticalLayout_4.setStretch(1, 125)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Slam Tracker", None))
        self.actionOd_poczatku.setText(QCoreApplication.translate("MainWindow", u"Powr\u00f3t", None))
        self.category.setText(QCoreApplication.translate("MainWindow", u"Imi\u0119 i nazwisko", None))
        self.category_2.setText(QCoreApplication.translate("MainWindow", u"Narodowo\u015b\u0107", None))
        self.category_3.setText(QCoreApplication.translate("MainWindow", u"Pierwszy mecz", None))
        self.category_4.setText(QCoreApplication.translate("MainWindow", u"Mecze rozegrane", None))
        self.category_5.setText(QCoreApplication.translate("MainWindow", u"Mecze wygrane", None))
        self.category_6.setText(QCoreApplication.translate("MainWindow", u"Mecze rozegrane na nawierzchni turnieju", None))
        self.category_7.setText(QCoreApplication.translate("MainWindow", u"Mecze wygrane na nawierzchni turnieju", None))
        self.category_8.setText(QCoreApplication.translate("MainWindow", u"Najwy\u017csze miejsce", None))
        self.category_9.setText(QCoreApplication.translate("MainWindow", u"Najwy\u017csze miejsce w poprzednich edycjach turnieju", None))
        self.category_10.setText(QCoreApplication.translate("MainWindow", u"Najwy\u017csze miejsce w turnieju wielkoszlemowym", None))
        self.category_11.setText(QCoreApplication.translate("MainWindow", u"Liczba tytu\u0142\u00f3w", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"*Wszystkie dane pochodz\u0105 z lat 2000-2015", None))
        self.player_1_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_1_nationality.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_1_first_match.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_1_matches_played.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_1_matches_won.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_1_same_surface_played.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_1_same_surface_won.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_1_best_finish.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_1_best_finish_tournament.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_1_best_finish_grand_slam.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_1_titles.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText("")
        self.player_2_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_nationality.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_first_match.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_matches_played.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_matches_won.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_same_surface_played.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_same_surface_won.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_best_finish.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_best_finish_tournament.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_best_finish_grand_slam.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.player_2_titles.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Nawigacja", None))
    # retranslateUi

