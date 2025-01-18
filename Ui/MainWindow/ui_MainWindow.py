# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QToolBar, QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(795, 630)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.action_import_images = QAction(MainWindow)
        self.action_import_images.setObjectName(u"action_import_images")
        icon = QIcon()
        icon.addFile(u":/icons/toolbar/toolbars/import_images.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_import_images.setIcon(icon)
        self.action_import_images.setMenuRole(QAction.MenuRole.NoRole)
        self.action_import_models = QAction(MainWindow)
        self.action_import_models.setObjectName(u"action_import_models")
        icon1 = QIcon()
        icon1.addFile(u":/icons/toolbar/toolbars/import_models.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_import_models.setIcon(icon1)
        self.action_import_models.setMenuRole(QAction.MenuRole.NoRole)
        self.action_check_infos = QAction(MainWindow)
        self.action_check_infos.setObjectName(u"action_check_infos")
        icon2 = QIcon()
        icon2.addFile(u":/icons/toolbar/toolbars/check_infos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_check_infos.setIcon(icon2)
        self.action_check_infos.setMenuRole(QAction.MenuRole.NoRole)
        self.action_analysis_report = QAction(MainWindow)
        self.action_analysis_report.setObjectName(u"action_analysis_report")
        icon3 = QIcon()
        icon3.addFile(u":/icons/toolbar/toolbars/analysis_report.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_analysis_report.setIcon(icon3)
        self.action_analysis_report.setMenuRole(QAction.MenuRole.NoRole)
        self.action_summon_report = QAction(MainWindow)
        self.action_summon_report.setObjectName(u"action_summon_report")
        icon4 = QIcon()
        icon4.addFile(u":/icons/toolbar/toolbars/summon_document.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_summon_report.setIcon(icon4)
        self.action_summon_report.setMenuRole(QAction.MenuRole.NoRole)
        self.action_set_analysis_path = QAction(MainWindow)
        self.action_set_analysis_path.setObjectName(u"action_set_analysis_path")
        icon5 = QIcon()
        icon5.addFile(u":/icons/toolbar/toolbars/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_set_analysis_path.setIcon(icon5)
        self.action_set_summon_path = QAction(MainWindow)
        self.action_set_summon_path.setObjectName(u"action_set_summon_path")
        self.action_set_summon_path.setIcon(icon5)
        self.action_import_folder = QAction(MainWindow)
        self.action_import_folder.setObjectName(u"action_import_folder")
        icon6 = QIcon()
        icon6.addFile(u":/icons/toolbar/toolbars/import_with_folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_import_folder.setIcon(icon6)
        self.action_import_folder.setMenuRole(QAction.MenuRole.NoRole)
        self.action_next_image = QAction(MainWindow)
        self.action_next_image.setObjectName(u"action_next_image")
        self.action_next_image.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(u":/icons/toolbar/toolbars/next.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_next_image.setIcon(icon7)
        self.action_next_image.setMenuRole(QAction.MenuRole.NoRole)
        self.action_prev_image = QAction(MainWindow)
        self.action_prev_image.setObjectName(u"action_prev_image")
        self.action_prev_image.setEnabled(False)
        icon8 = QIcon()
        icon8.addFile(u":/icons/toolbar/toolbars/prev.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_prev_image.setIcon(icon8)
        self.action_prev_image.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_select_picture = QWidget(self.centralwidget)
        self.widget_select_picture.setObjectName(u"widget_select_picture")
        self.horizontalLayout = QHBoxLayout(self.widget_select_picture)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget_selections = QListWidget(self.widget_select_picture)
        self.listWidget_selections.setObjectName(u"listWidget_selections")

        self.horizontalLayout.addWidget(self.listWidget_selections)


        self.horizontalLayout_3.addWidget(self.widget_select_picture)

        self.widget_display_main = QWidget(self.centralwidget)
        self.widget_display_main.setObjectName(u"widget_display_main")
        self.verticalLayout = QVBoxLayout(self.widget_display_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_display = QLabel(self.widget_display_main)
        self.label_display.setObjectName(u"label_display")

        self.verticalLayout.addWidget(self.label_display)


        self.horizontalLayout_3.addWidget(self.widget_display_main)

        self.operating_widget = QWidget(self.centralwidget)
        self.operating_widget.setObjectName(u"operating_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.operating_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.operate_tool_box = QToolBox(self.operating_widget)
        self.operate_tool_box.setObjectName(u"operate_tool_box")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 98, 124))
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_load_model = QPushButton(self.page)
        self.btn_load_model.setObjectName(u"btn_load_model")
        self.btn_load_model.setMinimumSize(QSize(0, 50))
        self.btn_load_model.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.btn_load_model)

        self.btn_load_image = QPushButton(self.page)
        self.btn_load_image.setObjectName(u"btn_load_image")
        self.btn_load_image.setMinimumSize(QSize(0, 50))
        self.btn_load_image.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btn_load_image)

        icon9 = QIcon()
        icon9.addFile(u":/icons/pagetables/pagetables/preload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.operate_tool_box.addItem(self.page, icon9, u"\u524d\u7f6e\u52a0\u8f7d")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 176, 182))
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget = QWidget(self.page_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_analysis_report = QLabel(self.widget)
        self.label_analysis_report.setObjectName(u"label_analysis_report")

        self.verticalLayout_7.addWidget(self.label_analysis_report)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_4)

        self.btn_set_analysis_path = QPushButton(self.widget)
        self.btn_set_analysis_path.setObjectName(u"btn_set_analysis_path")
        self.btn_set_analysis_path.setMinimumSize(QSize(0, 50))
        icon10 = QIcon()
        icon10.addFile(u":/icons/pagetables/pagetables/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_set_analysis_path.setIcon(icon10)

        self.verticalLayout_7.addWidget(self.btn_set_analysis_path)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.btn_analysis_report = QPushButton(self.widget)
        self.btn_analysis_report.setObjectName(u"btn_analysis_report")
        self.btn_analysis_report.setEnabled(False)
        self.btn_analysis_report.setMinimumSize(QSize(0, 50))
        icon11 = QIcon()
        icon11.addFile(u":/icons/pagetables/pagetables/analysis_report.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_analysis_report.setIcon(icon11)

        self.verticalLayout_7.addWidget(self.btn_analysis_report)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)


        self.verticalLayout_6.addWidget(self.widget)

        self.operate_tool_box.addItem(self.page_2, icon11, u"\u89e3\u6790\u7aef\u5c0f\u7a0b\u5e8f")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 144, 182))
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_summon_report = QWidget(self.page_3)
        self.widget_summon_report.setObjectName(u"widget_summon_report")
        self.verticalLayout_5 = QVBoxLayout(self.widget_summon_report)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_report_path = QLabel(self.widget_summon_report)
        self.label_report_path.setObjectName(u"label_report_path")

        self.verticalLayout_5.addWidget(self.label_report_path)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.btn_set_summon_path = QPushButton(self.widget_summon_report)
        self.btn_set_summon_path.setObjectName(u"btn_set_summon_path")
        self.btn_set_summon_path.setMinimumSize(QSize(0, 50))
        self.btn_set_summon_path.setIcon(icon10)

        self.verticalLayout_5.addWidget(self.btn_set_summon_path)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.btn_summon_report = QPushButton(self.widget_summon_report)
        self.btn_summon_report.setObjectName(u"btn_summon_report")
        self.btn_summon_report.setEnabled(False)
        self.btn_summon_report.setMinimumSize(QSize(0, 50))
        self.btn_summon_report.setIcon(icon4)

        self.verticalLayout_5.addWidget(self.btn_summon_report)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)


        self.verticalLayout_4.addWidget(self.widget_summon_report)

        icon12 = QIcon()
        icon12.addFile(u":/icons/pagetables/pagetables/summon_document.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.operate_tool_box.addItem(self.page_3, icon12, u"\u751f\u6210\u7aef\u5c0f\u7a0b\u5e8f")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 173, 387))
        self.horizontalLayout_4 = QHBoxLayout(self.page_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_param_browsing = QWidget(self.page_4)
        self.widget_param_browsing.setObjectName(u"widget_param_browsing")
        self.verticalLayout_3 = QVBoxLayout(self.widget_param_browsing)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.widget_param_browsing)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_4.addWidget(self.widget_param_browsing)

        icon13 = QIcon()
        icon13.addFile(u":/icons/pagetables/pagetables/recognize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.operate_tool_box.addItem(self.page_4, icon13, u"\u56fe\u50cf\u8bc6\u522b")

        self.horizontalLayout_2.addWidget(self.operate_tool_box)


        self.horizontalLayout_3.addWidget(self.operating_widget)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 795, 33))
        self.menu_import = QMenu(self.menubar)
        self.menu_import.setObjectName(u"menu_import")
        self.menu_check = QMenu(self.menubar)
        self.menu_check.setObjectName(u"menu_check")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_import.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_check.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu_import.addAction(self.action_import_images)
        self.menu_import.addAction(self.action_import_folder)
        self.menu_import.addSeparator()
        self.menu_import.addAction(self.action_import_models)
        self.menu_check.addAction(self.action_check_infos)
        self.menu.addAction(self.action_analysis_report)
        self.menu.addAction(self.action_set_analysis_path)
        self.menu_2.addAction(self.action_summon_report)
        self.menu_2.addAction(self.action_set_summon_path)
        self.menu_3.addAction(self.action_prev_image)
        self.menu_3.addAction(self.action_next_image)
        self.toolBar.addAction(self.action_import_images)
        self.toolBar.addAction(self.action_import_folder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_prev_image)
        self.toolBar.addAction(self.action_next_image)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_import_models)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_check_infos)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_analysis_report)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_summon_report)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.operate_tool_box.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5f69\u667a\u5feb\u8b66\u2014\u2014\u667a\u6167\u5f69\u8d85\u8f85\u52a9\u7cfb\u7edf", None))
        self.action_import_images.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u56fe\u50cf", None))
        self.action_import_models.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6a21\u578b", None))
#if QT_CONFIG(tooltip)
        self.action_import_models.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6a21\u578b", None))
#endif // QT_CONFIG(tooltip)
        self.action_check_infos.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.action_analysis_report.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u6790\u62a5\u544a", None))
        self.action_summon_report.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u62a5\u544a", None))
        self.action_set_analysis_path.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u89e3\u6790\u751f\u6210\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.action_set_summon_path.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u751f\u6210\u62a5\u544a\u8def\u5f84", None))
        self.action_import_folder.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6587\u4ef6\u5939", None))
        self.action_next_image.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20\u56fe\u50cf", None))
        self.action_prev_image.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20\u56fe\u50cf", None))
        self.label_display.setText("")
        self.btn_load_model.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6a21\u578b", None))
        self.btn_load_image.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u56fe\u50cf", None))
        self.operate_tool_box.setItemText(self.operate_tool_box.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u524d\u7f6e\u52a0\u8f7d", None))
        self.label_analysis_report.setText(QCoreApplication.translate("MainWindow", u"\u62a5\u544a\u89e3\u6790\u5c0f\u7a0b\u5e8f\u4f4d\u7f6e", None))
        self.btn_set_analysis_path.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u89e3\u6790\u62a5\u544a\u7684\u751f\u6210\u4f4d\u7f6e", None))
        self.btn_analysis_report.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u62a5\u544a", None))
        self.operate_tool_box.setItemText(self.operate_tool_box.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u89e3\u6790\u7aef\u5c0f\u7a0b\u5e8f", None))
        self.label_report_path.setText(QCoreApplication.translate("MainWindow", u"\u62a5\u544a\u751f\u6210\u8def\u5f84\u4f4d\u4e8e\uff1a", None))
        self.btn_set_summon_path.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u751f\u6210\u62a5\u544a\u8def\u5f84", None))
        self.btn_summon_report.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u62a5\u544a", None))
        self.operate_tool_box.setItemText(self.operate_tool_box.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"\u751f\u6210\u7aef\u5c0f\u7a0b\u5e8f", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bf4\u660e", None))
        self.operate_tool_box.setItemText(self.operate_tool_box.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u8bc6\u522b", None))
        self.menu_import.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.menu_check.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u89e3\u6790", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u822a", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

