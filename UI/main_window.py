from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import sys
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QMainWindow


sys.path.append("../ProjectUpdate")

from utils.load_data import load_data
from UI import search_result
from UI import level
from model.VideoTableModel import VideoTableModel
from model.ScrapeThread import ScraperThread
from model.StatThread import StatThread


class Ui_MainWindow(object):
    time = None
    data = []
    model = []
    levels = []
    result = []
    stats = []
    search_time = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(806, 495)
        MainWindow.setMinimumSize(1000, 500)
        MainWindow.setGeometry(180, 150, 1000, 500)
        MainWindow.setWindowTitle("Tube Harvest")
        MainWindow.setWindowIcon(QIcon("icon/logo.png"))
        MainWindow.showMaximized()
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 2, 0, 255), stop:1 rgba(0, 0, 0, 255));"
        )
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 2, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
            "border-color: rgb(0, 0, 0);"
        )
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Tabs = QtWidgets.QFrame(self.mainFrame)
        self.Tabs.setMinimumSize(QtCore.QSize(0, 0))
        self.Tabs.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Tabs.setStyleSheet(
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 2, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
            "background-color: rgb(255, 255, 255);"
        )
        self.Tabs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Tabs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Tabs.setObjectName("Tabs")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Tabs)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scraping_btn = QtWidgets.QPushButton(self.Tabs)
        self.scraping_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.scraping_btn.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.scraping_btn.setFont(font)
        self.scraping_btn.setObjectName("scraping_btn")
        self.horizontalLayout.addWidget(self.scraping_btn, 0, QtCore.Qt.AlignTop)
        self.main_btn = QtWidgets.QPushButton(self.Tabs)
        self.main_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.main_btn.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.main_btn.setFont(font)
        self.main_btn.setObjectName("main_btn")
        self.horizontalLayout.addWidget(self.main_btn, 0, QtCore.Qt.AlignTop)
        self.stat_btn = QtWidgets.QPushButton(self.Tabs)
        self.stat_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.stat_btn.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.stat_btn.setFont(font)
        self.stat_btn.setObjectName("stat_btn")
        self.horizontalLayout.addWidget(self.stat_btn, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.Tabs)
        self.stackedWidget = QtWidgets.QStackedWidget(self.mainFrame)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.logo = QtWidgets.QWidget()
        self.logo.setObjectName("logo")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.logo)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.stackedWidget.addWidget(self.logo)
        self.central_main = QtWidgets.QWidget()
        self.central_main.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(77, 77, 77, 255));"
        )
        self.central_main.setObjectName("central_main")
        self.gridLayout = QtWidgets.QGridLayout(self.central_main)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableView = QtWidgets.QTableView(self.central_main)
        self.tableView.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tableView.setFont(font)
        self.tableView.setStyleSheet("background: rgb(255, 255, 255)")
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.gridLayout.addLayout(self.verticalLayout_4, 1, 1, 1, 1)
        self.Side_panel = QtWidgets.QFrame(self.central_main)
        self.Side_panel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.Side_panel.setStyleSheet(
            "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 2, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 2, 0, 255), stop:1 rgba(0, 0, 0, 255));"
        )
        self.Side_panel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Side_panel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Side_panel.setObjectName("Side_panel")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Side_panel)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sorting_btn = QtWidgets.QPushButton(self.Side_panel)
        self.sorting_btn.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sorting_btn.setFont(font)
        self.sorting_btn.setStyleSheet("color : rgb(255, 255, 255)")
        self.sorting_btn.setObjectName("sorting_btn")
        self.verticalLayout_3.addWidget(self.sorting_btn)
        self.searching_btn = QtWidgets.QPushButton(self.Side_panel)
        self.searching_btn.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.searching_btn.setFont(font)
        self.searching_btn.setStyleSheet("color : rgb(255, 255, 255)")
        self.searching_btn.setObjectName("searching_btn")
        self.verticalLayout_3.addWidget(self.searching_btn)
        self.reset_btn = QtWidgets.QPushButton(self.Side_panel)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono SemiBold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.reset_btn.setFont(font)
        self.reset_btn.setStyleSheet("color : rgb(255, 255, 255)")
        self.reset_btn.setObjectName("reset_btn")
        self.verticalLayout_3.addWidget(self.reset_btn)
        self.gridLayout.addWidget(self.Side_panel, 0, 0, 1, 1)
        self.Options = QtWidgets.QFrame(self.central_main)
        self.Options.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Options.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(255, 255, 255, 255));"
        )
        self.Options.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Options.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Options.setObjectName("Options")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.Options)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.Options_stack = QtWidgets.QStackedWidget(self.Options)
        self.Options_stack.setObjectName("Options_stack")
        self.sorting = QtWidgets.QWidget()
        self.sorting.setObjectName("sorting")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.sorting)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.column_cb = QtWidgets.QComboBox(self.sorting)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.column_cb.setFont(font)
        self.column_cb.setObjectName("column_cb")
        self.column_cb.addItem("")
        self.column_cb.addItem("")
        self.column_cb.addItem("")
        self.column_cb.addItem("")
        self.column_cb.addItem("")
        self.column_cb.addItem("")
        self.column_cb.addItem("")
        self.column_cb.addItem("")
        self.column_cb.addItem("")
        self.gridLayout_2.addWidget(self.column_cb, 0, 0, 1, 2)
        self.algorithm_cb = QtWidgets.QComboBox(self.sorting)
        self.algorithm_cb.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.algorithm_cb.setFont(font)
        self.algorithm_cb.setObjectName("algorithm_cb")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.algorithm_cb.addItem("")
        self.gridLayout_2.addWidget(self.algorithm_cb, 0, 2, 1, 2)
        self.lvl_btn = QtWidgets.QPushButton(self.sorting)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lvl_btn.setFont(font)
        self.lvl_btn.setObjectName("lvl_btn")
        self.gridLayout_2.addWidget(self.lvl_btn, 0, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.sorting)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.time_lbl = QtWidgets.QLabel(self.sorting)
        self.time_lbl.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.time_lbl.setFont(font)
        self.time_lbl.setText("")
        self.time_lbl.setObjectName("time_lbl")
        self.gridLayout_2.addWidget(self.time_lbl, 1, 1, 1, 2)
        self.radioButton = QtWidgets.QRadioButton(self.sorting)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("ascending")
        self.gridLayout_2.addWidget(self.radioButton, 1, 3, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.sorting)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setChecked(False)
        self.radioButton_2.setObjectName("descending")
        self.gridLayout_2.addWidget(self.radioButton_2, 1, 4, 1, 1)
        self.lets_sort = QtWidgets.QPushButton(self.sorting)
        self.lets_sort.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lets_sort.setFont(font)
        self.lets_sort.setObjectName("lets_sort")
        self.gridLayout_2.addWidget(self.lets_sort, 0, 5, 2, 1)
        self.Options_stack.addWidget(self.sorting)
        self.search = QtWidgets.QWidget()
        self.search.setObjectName("search")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.search)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.column_cb_2 = QtWidgets.QComboBox(self.search)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.column_cb_2.setFont(font)
        self.column_cb_2.setObjectName("column_cb_2")
        self.column_cb_2.addItem("")
        self.column_cb_2.addItem("")
        self.column_cb_2.addItem("")
        self.column_cb_2.addItem("")
        self.column_cb_2.addItem("")
        self.column_cb_2.addItem("")
        self.column_cb_2.addItem("")
        self.column_cb_2.addItem("")
        self.column_cb_2.addItem("")
        self.gridLayout_3.addWidget(self.column_cb_2, 0, 0, 1, 2)
        self.algorithm_cb_2 = QtWidgets.QComboBox(self.search)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.algorithm_cb_2.setFont(font)
        self.algorithm_cb_2.setObjectName("algorithm_cb_2")
        self.algorithm_cb_2.addItem("")
        self.algorithm_cb_2.addItem("")
        self.algorithm_cb_2.addItem("")
        self.algorithm_cb_2.addItem("")
        self.algorithm_cb_2.addItem("")
        self.gridLayout_3.addWidget(self.algorithm_cb_2, 0, 2, 1, 2)
        self.filter_cb = QtWidgets.QComboBox(self.search)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filter_cb.setFont(font)
        self.filter_cb.setObjectName("filter_cb")
        self.filter_cb.addItem("")
        self.filter_cb.addItem("")
        self.filter_cb.addItem("")
        self.filter_cb.addItem("")
        self.gridLayout_3.addWidget(self.filter_cb, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.search)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        font = QtGui.QFont()
        font.setFamily("JetBrains Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_tb = QtWidgets.QLineEdit(self.search)
        self.search_tb.setMinimumSize(QtCore.QSize(35, 30))
        self.search_tb.setMaximumSize(QtCore.QSize(300, 16777215))
        self.search_tb.setFont(font)
        self.search_tb.setObjectName("search_tb")
        self.gridLayout_3.addWidget(self.search_tb, 1, 1, 1, 2)
        self.search_btn = QtWidgets.QPushButton(self.search)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_btn.setFont(font)
        self.search_btn.setObjectName("search_btn")
        self.gridLayout_3.addWidget(self.search_btn, 1, 3, 1, 2)
        self.Options_stack.addWidget(self.search)
        self.verticalLayout_5.addWidget(self.Options_stack)
        self.gridLayout.addWidget(self.Options, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.central_main)
        self.scraping = QtWidgets.QWidget()
        self.scraping.setObjectName("scraping")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scraping)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_btn = QtWidgets.QPushButton(self.scraping)
        self.start_btn.setMinimumSize(QtCore.QSize(10, 50))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start_btn.setFont(font)
        self.start_btn.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 10px;\n"
            "\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "        }\n"
            "\n"
            "QPushButton:hover {\n"
            "    color: red;\n"
            "        }\n"
            "QPushButton:pressed {\n"
            "    color: red;\n"
            "background-color:rgb(255, 255, 255)\n"
            "        }\n"
            ""
        )
        self.start_btn.setObjectName("start_btn")
        self.horizontalLayout_2.addWidget(self.start_btn)
        self.pause_btn = QtWidgets.QPushButton(self.scraping)
        self.pause_btn.setMinimumSize(QtCore.QSize(10, 50))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pause_btn.setFont(font)
        self.pause_btn.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 10px;\n"
            "\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "        }\n"
            "\n"
            "QPushButton:hover {\n"
            "    color: red;\n"
            "        }\n"
            "QPushButton:pressed {\n"
            "    color: red;\n"
            "background-color:rgb(255, 255, 255)\n"
            "        }\n"
            ""
        )
        self.pause_btn.setObjectName("pause_btn")
        self.horizontalLayout_2.addWidget(self.pause_btn)
        self.resume_btn = QtWidgets.QPushButton(self.scraping)
        self.resume_btn.setMinimumSize(QtCore.QSize(10, 50))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.resume_btn.setFont(font)
        self.resume_btn.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 10px;\n"
            "\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "        }\n"
            "\n"
            "QPushButton:hover {\n"
            "    color: red;\n"
            "        }\n"
            "QPushButton:pressed {\n"
            "    color: red;\n"
            "background-color:rgb(255, 255, 255)\n"
            "        }\n"
            ""
        )
        self.resume_btn.setObjectName("resume_btn")
        self.horizontalLayout_2.addWidget(self.resume_btn)
        self.stop_btn = QtWidgets.QPushButton(self.scraping)
        self.stop_btn.setMinimumSize(QtCore.QSize(10, 50))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stop_btn.setFont(font)
        self.stop_btn.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 10px;\n"
            "\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "        }\n"
            "\n"
            "QPushButton:hover {\n"
            "    color: red;\n"
            "        }\n"
            "QPushButton:pressed {\n"
            "    color: red;\n"
            "background-color:rgb(255, 255, 255)\n"
            "        }\n"
            ""
        )
        self.stop_btn.setObjectName("stop_btn")
        self.horizontalLayout_2.addWidget(self.stop_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.progressBar = QtWidgets.QProgressBar(self.scraping)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet(
            "QProgressBar\n"
            "{\n"
            "border: solid grey;\n"
            "border-radius: 10px;\n"
            "color: #ff0000;\n"
            "text-align : center;\n"
            "background-color: rgb(0, 0, 0);\n"
            "}\n"
            "QProgressBar::chunk \n"
            "{\n"
            "background-color: #888888;\n"
            "border-radius :10px;\n"
            "}  \n"
            ""
        )
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_6.addWidget(self.progressBar)
        self.stackedWidget.addWidget(self.scraping)
        self.stat = QtWidgets.QWidget()
        self.stat.setObjectName("stat")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.stat)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.stat)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.url1_tb = QtWidgets.QLineEdit(self.stat)
        self.url1_tb.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.url1_tb.setFont(font)
        self.url1_tb.setObjectName("url1_tb")
        self.verticalLayout_7.addWidget(self.url1_tb)
        self.label_4 = QtWidgets.QLabel(self.stat)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.url2_tb = QtWidgets.QLineEdit(self.stat)
        self.url2_tb.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.url2_tb.setFont(font)
        self.url2_tb.setObjectName("url2_tb")
        self.verticalLayout_7.addWidget(self.url2_tb)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.stat_btn_2 = QtWidgets.QPushButton(self.stat)
        self.stat_btn_2.setMinimumSize(QtCore.QSize(150, 35))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono NL SemiBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stat_btn_2.setFont(font)
        self.stat_btn_2.setStyleSheet(
            "QPushButton {\n"
            "border-radius: 10px;\n"
            "\n"
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "        }\n"
            "\n"
            "QPushButton:hover {\n"
            "    color: red;\n"
            "        }\n"
            "QPushButton:pressed {\n"
            "    color: red;\n"
            "background-color:rgb(255, 255, 255)\n"
            "        }\n"
            ""
        )
        self.stat_btn_2.setObjectName("stat_btn_2")
        self.verticalLayout_8.addWidget(self.stat_btn_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_8.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.stat)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        screen = self.stackedWidget.widget(0)
        screen.setStyleSheet(
            "background-image : url(icon/youtube.png); background-position: center;"
        )
        self.Options_stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # button connections
        self.scraping_btn.clicked.connect(self.show_scraping_page)
        self.main_btn.clicked.connect(self.show_main_page)
        self.stat_btn.clicked.connect(self.show_stat_page)
        self.sorting_btn.clicked.connect(self.show_sorting_page)
        self.searching_btn.clicked.connect(self.show_searching_page)
        self.lvl_btn.clicked.connect(self.show_level_window)
        self.lets_sort.clicked.connect(self.start_sorting)
        self.start_btn.clicked.connect(self.start_scraping)
        self.pause_btn.clicked.connect(self.pause_scraping)
        self.resume_btn.clicked.connect(self.resume_scraping)
        self.stop_btn.clicked.connect(self.stop_scraping)
        self.search_btn.clicked.connect(self.lets_search)
        self.reset_btn.clicked.connect(self.reset)
        self.stat_btn_2.clicked.connect(self.show_graphs)

        # load data
        self.data = load_data()
        self.set_data(self.data)

    def reset(self):
        self.search_btn.setEnabled(True)
        self.lets_sort.setEnabled(True)
        self.data = load_data()
        self.model.reset_data(self.data)

    def start_sorting(self):
        if self.algorithm_cb.currentText() == "--Select Algorithm--":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Select Algorithm ")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        elif self.column_cb.currentText() == "--Select Column--":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Select Column ")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        elif (
            self.column_cb.currentText() == "Channel"
            or self.column_cb.currentText() == "Title"
            or self.column_cb.currentText() == "URL"
        ) and (
            self.algorithm_cb.currentText() == "Counting Sort"
            or self.algorithm_cb.currentText() == "Radix Sort"
            or self.algorithm_cb.currentText() == "Bucket Sort"
            or self.algorithm_cb.currentText() == "Pigeon Sort"
            or self.algorithm_cb.currentText() == "Bead Sort"
        ):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("These sorting algorithms can't be used with this column")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        elif len(self.levels) == 0:
            col = self.column_cb.currentText()
            algo = self.algorithm_cb.currentText()
            if self.radioButton.isChecked():
                time_start = time.time()
                self.model.sort_by(0, len(self.data) - 1, col, algo, True)
                time_end = time.time()
                self.time_lbl.setText(str(time_end - time_start))
            else:
                time_start = time.time()
                self.model.sort_by(0, len(self.data) - 1, col, algo, False)
                time_end = time.time()
                self.time_lbl.setText(str(time_end - time_start))
            self.tableView.setModel(self.model)
            self.lets_sort.setEnabled(False)

    def start_scraping(self):
        self.start_btn.setEnabled(False)
        self.pause_btn.setEnabled(True)
        self.stop_btn.setEnabled(True)
        self.thread = ScraperThread()
        self.thread.data_ready.connect(self.update_progress_bar)
        self.thread.start()

    def pause_scraping(self):
        self.thread.pause()
        self.pause_btn.setEnabled(False)
        self.resume_btn.setEnabled(True)

    def resume_scraping(self):
        self.thread.resume()
        self.pause_btn.setEnabled(True)
        self.resume_btn.setEnabled(False)

    def stop_scraping(self):
        self.thread.stop()
        self.start_btn.setEnabled(True)
        self.pause_btn.setEnabled(False)
        self.resume_btn.setEnabled(False)
        self.stop_btn.setEnabled(False)

    def update_progress_bar(self, progress):
        self.progressBar.setValue(progress)
        if progress == 100:
            self.start_btn.setEnabled(True)
            self.pause_btn.setEnabled(False)
            self.resume_btn.setEnabled(False)
            self.stop_btn.setEnabled(False)

    def show_scraping_page(self):
        self.stackedWidget.setCurrentIndex(2)  # Show the scraping page

    def show_main_page(self):
        self.stackedWidget.setCurrentIndex(1)  # Show the main page

    def show_stat_page(self):
        self.stackedWidget.setCurrentIndex(3)  # Show the stat page

    def show_sorting_page(self):
        self.Options_stack.setCurrentIndex(0)  # Show the sorting page

    def show_searching_page(self):
        self.Options_stack.setCurrentIndex(1)  # Show the searching page

    def show_level_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = level.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.window = self.window
        self.window.show()
        self.ui.ok_btn.clicked.connect(self.get_levels)

    def get_levels(self):
        if (
            self.ui.lvl1_cb.currentText() != "--Select--"
            and self.ui.lvl2_cb.currentText() != "--Select--"
            and self.ui.lvl3_cb.currentText() != "--Select--"
        ):
            self.levels = [
                self.ui.lvl1_cb.currentText(),
                self.ui.lvl2_cb.currentText(),
                self.ui.lvl3_cb.currentText(),
            ]
            self.ui.hide()
            self.sort_multi()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Select all levels ")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def sort_multi(self):
        self.model.reset_data(self.data)
        if self.algorithm_cb.currentText() == "--Select Algorithm--":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Select Algorithm ")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        elif (
            self.algorithm_cb.currentText() == "Counting Sort"
            or self.algorithm_cb.currentText() == "Radix Sort"
            or self.algorithm_cb.currentText() == "Bucket Sort"
            or self.algorithm_cb.currentText() == "Pigeonhole Sort"
            or self.algorithm_cb.currentText() == "Bead Sort"
        ):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Selected algorithm can't be used with multi-level sorting")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        else:
            if self.radioButton.isChecked():
                algo = self.algorithm_cb.currentText()
                time_start = time.time()
                self.model.multi_lvl_sort(
                    0, len(self.data) - 1, self.levels, algo, True
                )
                time_end = time.time()
                self.time_lbl.setText(str(time_end - time_start))
            else:
                algo = self.algorithm_cb.currentText()
                time_start = time.time()
                self.model.multi_lvl_sort(
                    0, len(self.data) - 1, self.levels, algo, False
                )
                time_end = time.time()
                self.time_lbl.setText(str(time_end - time_start))
            self.tableView.setModel(self.model)
            self.levels = []

    def show_searching_result(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = search_result.Ui_MainWindow()
        self.ui.setupUi(self.window, self.result, self.search_time)
        self.window.show()

    def lets_search(self):
        self.search_btn.setEnabled(False)
        if self.algorithm_cb_2.currentText() == "--Select Algorithm--":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Select Algorithm ")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        elif self.search_tb.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Enter the search key ")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        else:
            col = self.column_cb_2.currentText()
            algo = self.algorithm_cb_2.currentText()
            target = self.search_tb.text()
            filter = self.filter_cb.currentText()
            start_time = time.time()

            if col != "--Select Column--":
                self.result = self.model.search_by(
                    0,
                    len(self.data) - 1,
                    algo,
                    target,
                    filter,
                    col,
                )
            else:
                self.result = self.model.search_multicolumn(
                    0,
                    len(self.data) - 1,
                    algo,
                    target,
                    filter,
                )

            end_time = time.time()
            self.search_time = str(end_time - start_time)
            if len(self.result) == 0:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("No result found")
                msg.setWindowTitle("Warning")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
            elif len(self.result) == 1:
                self.show_searching_result()
            else:
                self.model.reset_data(self.result)
                self.label.setText(self.search_time)

    def set_data(self, data):
        header = [
            "URL",
            "Channel",
            "Subscribers",
            "Title",
            "Likes",
            "Duration",
            "Views",
            "Comments",
        ]
        self.model = VideoTableModel(data, header)
        self.tableView.setModel(self.model)
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        self.tableView.setColumnWidth(0, 200)

    def show_graphs(self):
        if self.url1_tb.text() == "" or self.url2_tb.text() == "":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Enter the URLs ")
            msg.setWindowTitle("Warning")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
        else:
            urls = [self.url1_tb.text(), self.url2_tb.text()]
            time.sleep(3)
            self.thread = StatThread(urls)
            self.stats = self.thread.run()
            self.display_graphs()

    def display_graphs(self):
        # Create sample data for the bar graphs
        categories = [
            "Video 1",
            "Video 2",
        ]

        # Create Matplotlib figures and add bar plots
        fig, axs = plt.subplots(2, 2, figsize=(12, 4), constrained_layout=True)
        time.sleep(3)
        axs[0,0].bar(categories, [self.stats[0][0], self.stats[1][0]])
        axs[0,0].set_title("Subscribers")

        axs[0,1].bar(categories, [self.stats[0][2], self.stats[1][2]])
        axs[0,1].set_title("Views")

        axs[1,0].bar(categories, [self.stats[0][3], self.stats[1][3]])
        axs[1,0].set_title("Comments")

        axs[1,1].bar(categories, [self.stats[0][1], self.stats[1][1]])
        axs[1,1].set_title("Duration")

        # Embed Matplotlib figure into a PyQt5 frame
        canvas = FigureCanvas(fig)

        self.graph_window = QMainWindow()
        self.graph_window.setCentralWidget(canvas)
        self.graph_window.setGeometry(200, 200, 1000, 600)
        self.graph_window.setWindowTitle("Graphs Window")
        self.graph_window.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TubeHarvest"))
        self.scraping_btn.setText(_translate("MainWindow", "Scraping"))
        self.main_btn.setText(_translate("MainWindow", "Main"))
        self.stat_btn.setText(_translate("MainWindow", "Stat"))
        self.stackedWidget.setToolTip(
            _translate(
                "MainWindow",
                '<html><head/><body><p><img src=":/youtube/youtube.png"/><img src=":/youtube/youtube.png"/></p></body></html>',
            )
        )
        self.sorting_btn.setText(_translate("MainWindow", "Sorting"))
        self.searching_btn.setText(_translate("MainWindow", "Searching"))
        self.reset_btn.setText(_translate("MainWindow", "Reset"))

        self.column_cb.setItemText(0, _translate("MainWindow", "--Select Column--"))
        self.column_cb.setItemText(1, _translate("MainWindow", "URL"))
        self.column_cb.setItemText(2, _translate("MainWindow", "Channel"))
        self.column_cb.setItemText(3, _translate("MainWindow", "Subscribers"))
        self.column_cb.setItemText(4, _translate("MainWindow", "Title"))
        self.column_cb.setItemText(5, _translate("MainWindow", "Likes"))
        self.column_cb.setItemText(6, _translate("MainWindow", "Duration"))
        self.column_cb.setItemText(7, _translate("MainWindow", "Views"))
        self.column_cb.setItemText(8, _translate("MainWindow", "Comments"))

        self.algorithm_cb.setItemText(
            0, _translate("MainWindow", "--Select Algorithm--")
        )
        self.algorithm_cb.setItemText(1, _translate("MainWindow", "Selection Sort"))
        self.algorithm_cb.setItemText(2, _translate("MainWindow", "Bubble Sort"))
        self.algorithm_cb.setItemText(3, _translate("MainWindow", "Insertion Sort"))
        self.algorithm_cb.setItemText(4, _translate("MainWindow", "Merge Sort"))
        self.algorithm_cb.setItemText(5, _translate("MainWindow", "Quick Sort"))
        self.algorithm_cb.setItemText(6, _translate("MainWindow", "Heap Sort"))
        self.algorithm_cb.setItemText(7, _translate("MainWindow", "Brick Sort"))
        self.algorithm_cb.setItemText(8, _translate("MainWindow", "Counting Sort"))
        self.algorithm_cb.setItemText(9, _translate("MainWindow", "Radix Sort"))
        self.algorithm_cb.setItemText(10, _translate("MainWindow", "Bucket Sort"))
        self.algorithm_cb.setItemText(11, _translate("MainWindow", "PigeonHole Sort"))
        self.algorithm_cb.setItemText(12, _translate("MainWindow", "Bead Sort"))

        self.column_cb_2.setItemText(0, _translate("MainWindow", "--Select Column--"))
        self.column_cb_2.setItemText(1, _translate("MainWindow", "URL"))
        self.column_cb_2.setItemText(2, _translate("MainWindow", "Channel"))
        self.column_cb_2.setItemText(3, _translate("MainWindow", "Subscribers"))
        self.column_cb_2.setItemText(4, _translate("MainWindow", "Title"))
        self.column_cb_2.setItemText(5, _translate("MainWindow", "Likes"))
        self.column_cb_2.setItemText(6, _translate("MainWindow", "Duration"))
        self.column_cb_2.setItemText(7, _translate("MainWindow", "Views"))
        self.column_cb_2.setItemText(8, _translate("MainWindow", "Comments"))

        self.algorithm_cb_2.setItemText(
            0, _translate("MainWindow", "--Select Algorithm--")
        )
        self.algorithm_cb_2.setItemText(1, _translate("MainWindow", "Linear Search"))
        self.algorithm_cb_2.setItemText(2, _translate("MainWindow", "Binary Search"))
        self.algorithm_cb_2.setItemText(3, _translate("MainWindow", "Jump Search"))
        self.algorithm_cb_2.setItemText(
            4, _translate("MainWindow", "Exponential Search")
        )

        self.filter_cb.setItemText(0, _translate("MainWindow", "--Select filter--"))
        self.filter_cb.setItemText(1, _translate("MainWindow", "Starts With"))
        self.filter_cb.setItemText(2, _translate("MainWindow", "Ends With"))
        self.filter_cb.setItemText(3, _translate("MainWindow", "Contains"))

        self.lvl_btn.setText(_translate("MainWindow", "Select Level"))
        self.label_2.setText(_translate("MainWindow", "Time Taken"))
        self.radioButton.setText(_translate("MainWindow", "Ascending"))
        self.radioButton_2.setText(_translate("MainWindow", "Descending"))
        self.lets_sort.setText(_translate("MainWindow", "Sort"))
        self.label.setText(_translate("MainWindow", "Search"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.pause_btn.setText(_translate("MainWindow", "Pause"))
        self.resume_btn.setText(_translate("MainWindow", "Resume"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.label_3.setText(_translate("MainWindow", "Enter URL1"))
        self.label_4.setText(_translate("MainWindow", "Enter URL2"))
        self.stat_btn_2.setText(_translate("MainWindow", "Show Stat"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.ui = Ui_MainWindow()
    window.ui.setupUi(window)
    window.show()
    sys(exit(app.exec_()))
