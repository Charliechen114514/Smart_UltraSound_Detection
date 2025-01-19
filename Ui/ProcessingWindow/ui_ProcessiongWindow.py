# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProcessiongWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

class Ui_ProcessingWindow(object):
    def setupUi(self, ProcessingWindow):
        if not ProcessingWindow.objectName():
            ProcessingWindow.setObjectName(u"ProcessingWindow")
        ProcessingWindow.resize(810, 670)
        self.centralwidget = QWidget(ProcessingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_detection = QWidget(self.centralwidget)
        self.widget_detection.setObjectName(u"widget_detection")
        self.horizontalLayout = QHBoxLayout(self.widget_detection)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_recognize_info = QLabel(self.widget_detection)
        self.label_recognize_info.setObjectName(u"label_recognize_info")

        self.horizontalLayout.addWidget(self.label_recognize_info)

        self.recognize_progressBar = QProgressBar(self.widget_detection)
        self.recognize_progressBar.setObjectName(u"recognize_progressBar")
        self.recognize_progressBar.setStyleSheet(u"QProgressBar {\n"
"    text-align: center;\n"
"    height: 30px;\n"
"    border-radius: 15px;\n"
"    background: #e6f2ff;  /* \u80cc\u666f\u989c\u8272\uff1a\u6de1\u84dd\u8272 */\n"
"    border: 2px solid #a3c2f5;  /* \u8fb9\u6846\u989c\u8272\uff1a\u6df1\u4e00\u4e9b\u7684\u84dd\u8272 */\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 15px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
"                                stop:0 rgba(173, 216, 230, 255), \n"
"                                stop:0.5 rgba(135, 206, 250, 255), \n"
"                                stop:1 rgba(0, 191, 255, 255));  /* \u6de1\u84dd\u8272\u5230\u4eae\u84dd\u8272\u7684\u6e10\u53d8 */\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QProgressBar:focus {\n"
"    border: 2px solid #3399ff;  /* \u83b7\u5f97\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #b3d9ff;\n"
"    border: 2px solid #66a3ff;\n"
"    border-radius: 10px;\n"
"    pa"
                        "dding: 10px;\n"
"    color: #333333;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #80c4ff;\n"
"}\n"
"")
        self.recognize_progressBar.setMaximum(100)
        self.recognize_progressBar.setValue(0)

        self.horizontalLayout.addWidget(self.recognize_progressBar)

        self.label_show_recognize_left = QLabel(self.widget_detection)
        self.label_show_recognize_left.setObjectName(u"label_show_recognize_left")

        self.horizontalLayout.addWidget(self.label_show_recognize_left)


        self.verticalLayout_2.addWidget(self.widget_detection)

        self.widget_detection_2 = QWidget(self.centralwidget)
        self.widget_detection_2.setObjectName(u"widget_detection_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_detection_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_summon_info = QLabel(self.widget_detection_2)
        self.label_summon_info.setObjectName(u"label_summon_info")

        self.horizontalLayout_2.addWidget(self.label_summon_info)

        self.summon_progressBar = QProgressBar(self.widget_detection_2)
        self.summon_progressBar.setObjectName(u"summon_progressBar")
        self.summon_progressBar.setStyleSheet(u"QProgressBar {\n"
"    text-align: center;\n"
"    height: 30px;\n"
"    border-radius: 15px;\n"
"    background: #e6f2ff;  /* \u80cc\u666f\u989c\u8272\uff1a\u6de1\u84dd\u8272 */\n"
"    border: 2px solid #a3c2f5;  /* \u8fb9\u6846\u989c\u8272\uff1a\u6df1\u4e00\u4e9b\u7684\u84dd\u8272 */\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 15px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
"                                stop:0 rgba(173, 216, 230, 255), \n"
"                                stop:0.5 rgba(135, 206, 250, 255), \n"
"                                stop:1 rgba(0, 191, 255, 255));  /* \u6de1\u84dd\u8272\u5230\u4eae\u84dd\u8272\u7684\u6e10\u53d8 */\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QProgressBar:focus {\n"
"    border: 2px solid #3399ff;  /* \u83b7\u5f97\u7126\u70b9\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #b3d9ff;\n"
"    border: 2px solid #66a3ff;\n"
"    border-radius: 10px;\n"
"    pa"
                        "dding: 10px;\n"
"    color: #333333;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #80c4ff;\n"
"}\n"
"")
        self.summon_progressBar.setMaximum(100)
        self.summon_progressBar.setValue(0)

        self.horizontalLayout_2.addWidget(self.summon_progressBar)

        self.label_summon_show_left = QLabel(self.widget_detection_2)
        self.label_summon_show_left.setObjectName(u"label_summon_show_left")

        self.horizontalLayout_2.addWidget(self.label_summon_show_left)


        self.verticalLayout_2.addWidget(self.widget_detection_2)

        self.result_show = QTextBrowser(self.centralwidget)
        self.result_show.setObjectName(u"result_show")
        self.result_show.setStyleSheet(u"QTextBrowser {\n"
"    border: 2px solid #B0C4DE;\n"
"    border-radius: 10px;\n"
"    background: #F0F8FF;\n"
"    color: #4682B4;\n"
"    font-size: 14px;\n"
"    padding: 10px;\n"
"    selection-background-color: #87CEEB;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QTextBrowser:disabled {\n"
"    background: #E0FFFF;\n"
"    color: #A9A9A9;\n"
"    border: 2px solid #A9A9A9;\n"
"}\n"
"\n"
"QTextBrowser:focus {\n"
"    border: 2px solid #ADD8E6;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.result_show)

        self.widget_operate = QWidget(self.centralwidget)
        self.widget_operate.setObjectName(u"widget_operate")
        self.verticalLayout = QVBoxLayout(self.widget_operate)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_continue_summon_report = QPushButton(self.widget_operate)
        self.btn_continue_summon_report.setObjectName(u"btn_continue_summon_report")
        self.btn_continue_summon_report.setEnabled(False)
        self.btn_continue_summon_report.setMinimumSize(QSize(0, 50))
        self.btn_continue_summon_report.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #B0C4DE;\n"
"    border-radius: 10px;\n"
"    background: #F0F8FF;\n"
"    color: #4682B4;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    padding: 6px 12px;\n"
"    text-align: center;\n"
"    cursor: pointer;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: #E0FFFF;\n"
"    border: 2px solid #87CEEB;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #87CEEB;\n"
"    border: 2px solid #4682B4;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: #E0FFFF;\n"
"    color: #A9A9A9;\n"
"    border: 2px solid #A9A9A9;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"    border: 2px solid #ADD8E6;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.btn_continue_summon_report)


        self.verticalLayout_2.addWidget(self.widget_operate)

        ProcessingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ProcessingWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 810, 33))
        ProcessingWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ProcessingWindow)
        self.statusbar.setObjectName(u"statusbar")
        ProcessingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ProcessingWindow)

        QMetaObject.connectSlotsByName(ProcessingWindow)
    # setupUi

    def retranslateUi(self, ProcessingWindow):
        ProcessingWindow.setWindowTitle(QCoreApplication.translate("ProcessingWindow", u"\u62a5\u544a\u8fdb\u5ea6", None))
        self.label_recognize_info.setText(QCoreApplication.translate("ProcessingWindow", u"\u5f53\u524d\u8bc6\u522b\u8fdb\u5ea6", None))
        self.label_show_recognize_left.setText(QCoreApplication.translate("ProcessingWindow", u"0 | 0", None))
        self.label_summon_info.setText(QCoreApplication.translate("ProcessingWindow", u"\u5f53\u524d\u62a5\u544a\u751f\u6210\u8fdb\u5ea6", None))
        self.label_summon_show_left.setText(QCoreApplication.translate("ProcessingWindow", u"0 | 0", None))
        self.btn_continue_summon_report.setText(QCoreApplication.translate("ProcessingWindow", u"\u751f\u6210\u62a5\u544a", None))
    # retranslateUi

