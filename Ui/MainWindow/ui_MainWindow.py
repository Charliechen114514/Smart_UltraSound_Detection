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
        MainWindow.resize(1109, 905)
        MainWindow.setStyleSheet(u"")
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
        self.action_analysis_report.setEnabled(True)
        icon3 = QIcon()
        icon3.addFile(u":/icons/toolbar/toolbars/analysis_report.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_analysis_report.setIcon(icon3)
        self.action_analysis_report.setMenuRole(QAction.MenuRole.NoRole)
        self.action_summon_report_for_current = QAction(MainWindow)
        self.action_summon_report_for_current.setObjectName(u"action_summon_report_for_current")
        self.action_summon_report_for_current.setEnabled(False)
        icon4 = QIcon()
        icon4.addFile(u":/icons/toolbar/toolbars/summon_document.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_summon_report_for_current.setIcon(icon4)
        self.action_summon_report_for_current.setMenuRole(QAction.MenuRole.NoRole)
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
        self.action_summon_report_for_all = QAction(MainWindow)
        self.action_summon_report_for_all.setObjectName(u"action_summon_report_for_all")
        self.action_summon_report_for_all.setEnabled(False)
        icon9 = QIcon()
        icon9.addFile(u":/icons/pagetables/pagetables/summon_document.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_summon_report_for_all.setIcon(icon9)
        self.action_summon_report_for_all.setMenuRole(QAction.MenuRole.NoRole)
        self.action_summon_selectMulti = QAction(MainWindow)
        self.action_summon_selectMulti.setObjectName(u"action_summon_selectMulti")
        self.action_summon_selectMulti.setEnabled(False)
        self.action_summon_selectMulti.setIcon(icon4)
        self.action_summon_selectMulti.setMenuRole(QAction.MenuRole.NoRole)
        self.action_clear = QAction(MainWindow)
        self.action_clear.setObjectName(u"action_clear")
        icon10 = QIcon()
        icon10.addFile(u":/icons/toolbar/toolbars/clear_images.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_clear.setIcon(icon10)
        self.action_clear.setMenuRole(QAction.MenuRole.NoRole)
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
        self.listWidget_selections.setStyleSheet(u"QListWidget {\n"
"    background-color: #f4f8fd; /* \u80cc\u666f\u989c\u8272\uff1a\u6de1\u84dd\u8272 */\n"
"    border: 2px solid #a3c2f5; /* \u8fb9\u6846\u989c\u8272\uff1a\u6df1\u84dd\u8272 */\n"
"    border-radius: 12px; /* \u5706\u89d2\u6548\u679c */\n"
"    font-size: 14px;\n"
"    color: #4682B4; /* \u9ed8\u8ba4\u6587\u672c\u989c\u8272\uff1a\u6df1\u84dd\u8272 */\n"
"    padding: 8px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    background-color: transparent;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    margin: 4px;\n"
"    font-size: 14px;\n"
"    color: #4682B4; /* \u9879\u76ee\u9879\u7684\u6587\u672c\u989c\u8272 */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, \n"
"                                stop:0 rgba(135, 206, 250, 255), \n"
"                                stop:1 rgba(0, 191, 255, 255)); /* \u9009\u4e2d\u9879\u7684\u6e10\u53d8\u80cc\u666f */\n"
"    color: white; /* \u9009\u4e2d\u9879\u7684"
                        "\u6587\u672c\u989c\u8272 */\n"
"    border-radius: 8px;\n"
"    border: 2px solid #3399ff; /* \u589e\u52a0\u8fb9\u6846\u7a81\u51fa\u9009\u4e2d\u9879 */\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"    background-color: #b3d9ff; /* \u60ac\u505c\u9879\u7684\u80cc\u666f\uff1a\u6d45\u84dd\u8272 */\n"
"    color: #0066cc; /* \u60ac\u505c\u9879\u7684\u6587\u672c\u989c\u8272 */\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QListWidget::item:focus {\n"
"    border: 2px solid #3399ff; /* \u7126\u70b9\u9879\u7684\u8fb9\u6846\u989c\u8272 */\n"
"}\n"
"\n"
"QScrollBar:vertical, QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #f4f8fd;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border-radius: 6px;\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background: #80c4ff;\n"
"    border-radius: 6px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {\n"
"    background: #3399ff; /* \u6eda\u52a8"
                        "\u6761\u60ac\u505c\u65f6\u80cc\u666f\uff1a\u4eae\u84dd\u8272 */\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical,\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QListWidget QScrollBar {\n"
"    margin: 6px;\n"
"}\n"
"")

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
        self.verticalLayout_5 = QVBoxLayout(self.operating_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.operate_tool_box = QToolBox(self.operating_widget)
        self.operate_tool_box.setObjectName(u"operate_tool_box")
        self.operate_tool_box.setStyleSheet(u"QToolBox {\n"
"    background-color: #f4f8fd; /* \u80cc\u666f\u989c\u8272\uff1a\u6de1\u84dd\u8272 */\n"
"    border: 2px solid #a3c2f5; /* \u8fb9\u6846\u989c\u8272\uff1a\u6df1\u84dd\u8272 */\n"
"    border-radius: 12px; /* \u5706\u89d2\u6548\u679c */\n"
"    font-size: 12px; /* \u6062\u590d\u5b57\u4f53\u5927\u5c0f\u4e3a 12px */\n"
"    color: #4682B4; /* \u9ed8\u8ba4\u6587\u672c\u989c\u8272\uff1a\u6df1\u84dd\u8272 */\n"
"    padding: 10px;\n"
"    outline: none;\n"
"}\n"
"\n"
"QToolBox::tab-bar {\n"
"    alignment: center;\n"
"    margin: 4px;\n"
"}\n"
"\n"
"QToolBox::tab:hover {\n"
"    background-color: #b3d9ff; /* \u6807\u7b7e\u60ac\u505c\u65f6\u80cc\u666f\uff1a\u6d45\u84dd\u8272 */\n"
"    color: #0066cc; /* \u6807\u7b7e\u60ac\u505c\u65f6\u6587\u5b57\uff1a\u6df1\u84dd\u8272 */\n"
"}\n"
"\n"
"QToolBox::tab:selected {\n"
"    background-color: #80c4ff; /* \u9009\u4e2d\u6807\u7b7e\u7684\u80cc\u666f\uff1a\u4eae\u84dd\u8272 */\n"
"    color: white; /* \u9009\u4e2d\u6807\u7b7e\u7684\u6587\u5b57\uff1a\u767d\u8272"
                        " */\n"
"    border: 2px solid #3399ff; /* \u9009\u4e2d\u6807\u7b7e\u7684\u8fb9\u6846\u989c\u8272\uff1a\u4eae\u84dd\u8272 */\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QToolBox::panel {\n"
"    background-color: #f4f8fd; /* \u9762\u677f\u80cc\u666f\uff1a\u6de1\u84dd\u8272 */\n"
"    border: 2px solid #a3c2f5; /* \u9762\u677f\u8fb9\u6846\uff1a\u6df1\u84dd\u8272 */\n"
"    border-radius: 12px; /* \u9762\u677f\u5706\u89d2 */\n"
"    padding: 10px;\n"
"    margin-top: 0px; /* \u907f\u514d\u6298\u53e0\u540e\u4ea7\u751f\u4e0d\u5fc5\u8981\u7684\u4e0a\u8fb9\u8ddd */\n"
"}\n"
"\n"
"QToolBox::page {\n"
"    background-color: #f4f8fd; /* \u9875\u9762\u80cc\u666f\uff1a\u6de1\u84dd\u8272 */\n"
"    border-radius: 10px; /* \u9875\u9762\u5706\u89d2 */\n"
"    padding: 8px 15px; /* \u8c03\u6574\u5185\u8fb9\u8ddd\uff0c\u907f\u514d\u906e\u6321 */\n"
"    color: #4682B4; /* \u9875\u9762\u6587\u5b57\u989c\u8272\uff1a\u6df1\u84dd\u8272 */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #4682B4; /* \u6807\u7b7e\u6587\u5b57\u989c\u8272\uff1a\u6df1"
                        "\u84dd\u8272 */\n"
"    font-size: 14px; /* \u8c03\u6574\u6807\u7b7e\u6587\u5b57\u5927\u5c0f\u4e3a 14px */\n"
"    padding: 10px;\n"
"    background-color: #e6f2ff; /* \u6807\u7b7e\u80cc\u666f\u989c\u8272\uff1a\u6de1\u84dd\u8272 */\n"
"    border-radius: 8px; /* \u5706\u89d2\u6548\u679c */\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    background-color: #b3d9ff; /* \u60ac\u505c\u65f6\u80cc\u666f\uff1a\u6d45\u84dd\u8272 */\n"
"    color: #0066cc; /* \u60ac\u505c\u65f6\u6587\u5b57\u989c\u8272\uff1a\u6df1\u84dd\u8272 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #b3d9ff; /* \u6309\u94ae\u80cc\u666f\u989c\u8272\uff1a\u6de1\u84dd\u8272 */\n"
"    border: 2px solid #66a3ff; /* \u6309\u94ae\u8fb9\u6846\u989c\u8272\uff1a\u6d45\u84dd\u8272 */\n"
"    border-radius: 12px; /* \u6309\u94ae\u5706\u89d2 */\n"
"    padding: 10px 18px; /* \u8c03\u6574\u6309\u94ae\u5185\u8fb9\u8ddd */\n"
"    font-size: 14px; /* \u6309\u94ae\u6587\u5b57\u5927\u5c0f\uff1a14px */\n"
"    color: #333333; /* \u6309\u94ae\u6587\u5b57\u989c\u8272"
                        "\uff1a\u6df1\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #80c4ff; /* \u60ac\u505c\u65f6\u80cc\u666f\u989c\u8272\uff1a\u4eae\u84dd\u8272 */\n"
"    border: 2px solid #3399ff; /* \u60ac\u505c\u65f6\u8fb9\u6846\u989c\u8272\uff1a\u4eae\u84dd\u8272 */\n"
"    color: #ffffff; /* \u60ac\u505c\u65f6\u6587\u5b57\u989c\u8272\uff1a\u767d\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3399ff; /* \u6309\u94ae\u88ab\u6309\u4e0b\u65f6\u7684\u80cc\u666f\uff1a\u4eae\u84dd\u8272 */\n"
"    border: 2px solid #66a3ff; /* \u88ab\u6309\u4e0b\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"    color: white; /* \u6309\u94ae\u6587\u5b57\u989c\u8272\uff1a\u767d\u8272 */\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #e0e0e0; /* \u7981\u7528\u65f6\u7684\u80cc\u666f\uff1a\u7070\u8272 */\n"
"    color: #a9a9a9; /* \u7981\u7528\u65f6\u7684\u6587\u5b57\u989c\u8272\uff1a\u7070\u8272 */\n"
"    border: 2px solid #d0d0d0; /* \u7981\u7528\u65f6\u7684\u8fb9\u6846\uff1a\u7070\u8272 *"
                        "/\n"
"}\n"
"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 134, 136))
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_8)

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

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_9)

        icon11 = QIcon()
        icon11.addFile(u":/icons/pagetables/pagetables/preload.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.operate_tool_box.addItem(self.page, icon11, u"\u524d\u7f6e\u52a0\u8f7d")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 212, 306))
        self.verticalLayout_6 = QVBoxLayout(self.page_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_analysis_report = QLabel(self.page_2)
        self.label_analysis_report.setObjectName(u"label_analysis_report")
        self.label_analysis_report.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_analysis_report)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.btn_set_analysis_path = QPushButton(self.page_2)
        self.btn_set_analysis_path.setObjectName(u"btn_set_analysis_path")
        self.btn_set_analysis_path.setMinimumSize(QSize(0, 50))
        icon12 = QIcon()
        icon12.addFile(u":/icons/pagetables/pagetables/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_set_analysis_path.setIcon(icon12)

        self.verticalLayout_6.addWidget(self.btn_set_analysis_path)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)

        self.btn_analysis_report = QPushButton(self.page_2)
        self.btn_analysis_report.setObjectName(u"btn_analysis_report")
        self.btn_analysis_report.setEnabled(False)
        self.btn_analysis_report.setMinimumSize(QSize(0, 50))
        icon13 = QIcon()
        icon13.addFile(u":/icons/pagetables/pagetables/analysis_report.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_analysis_report.setIcon(icon13)

        self.verticalLayout_6.addWidget(self.btn_analysis_report)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.operate_tool_box.addItem(self.page_2, icon13, u"\u89e3\u6790\u7aef\u5c0f\u7a0b\u5e8f")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 226, 502))
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_report_path = QLabel(self.page_3)
        self.label_report_path.setObjectName(u"label_report_path")
        self.label_report_path.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_report_path)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.btn_set_summon_path = QPushButton(self.page_3)
        self.btn_set_summon_path.setObjectName(u"btn_set_summon_path")
        self.btn_set_summon_path.setMinimumSize(QSize(0, 50))
        self.btn_set_summon_path.setIcon(icon12)

        self.verticalLayout_4.addWidget(self.btn_set_summon_path)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.btn_summon_report_for_current = QPushButton(self.page_3)
        self.btn_summon_report_for_current.setObjectName(u"btn_summon_report_for_current")
        self.btn_summon_report_for_current.setEnabled(False)
        self.btn_summon_report_for_current.setMinimumSize(QSize(0, 50))
        self.btn_summon_report_for_current.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.btn_summon_report_for_current)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.btn_summon_report_for_all = QPushButton(self.page_3)
        self.btn_summon_report_for_all.setObjectName(u"btn_summon_report_for_all")
        self.btn_summon_report_for_all.setEnabled(False)
        self.btn_summon_report_for_all.setMinimumSize(QSize(0, 50))
        self.btn_summon_report_for_all.setIcon(icon9)

        self.verticalLayout_4.addWidget(self.btn_summon_report_for_all)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)

        self.btn_summon_select_multi = QPushButton(self.page_3)
        self.btn_summon_select_multi.setObjectName(u"btn_summon_select_multi")

        self.verticalLayout_4.addWidget(self.btn_summon_select_multi)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_12)

        self.operate_tool_box.addItem(self.page_3, icon9, u"\u751f\u6210\u7aef\u5c0f\u7a0b\u5e8f")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 228, 638))
        self.horizontalLayout_4 = QHBoxLayout(self.page_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_param_browsing = QWidget(self.page_4)
        self.widget_param_browsing.setObjectName(u"widget_param_browsing")
        self.verticalLayout_3 = QVBoxLayout(self.widget_param_browsing)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_soundinfo = QLabel(self.widget_param_browsing)
        self.label_soundinfo.setObjectName(u"label_soundinfo")

        self.verticalLayout_3.addWidget(self.label_soundinfo)

        self.btn_check_indications = QPushButton(self.widget_param_browsing)
        self.btn_check_indications.setObjectName(u"btn_check_indications")
        self.btn_check_indications.setIcon(icon2)

        self.verticalLayout_3.addWidget(self.btn_check_indications)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)

        self.btn_audio_control = QPushButton(self.widget_param_browsing)
        self.btn_audio_control.setObjectName(u"btn_audio_control")

        self.verticalLayout_3.addWidget(self.btn_audio_control)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)


        self.horizontalLayout_4.addWidget(self.widget_param_browsing)

        icon14 = QIcon()
        icon14.addFile(u":/icons/pagetables/pagetables/recognize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.operate_tool_box.addItem(self.page_4, icon14, u"\u8bed\u97f3\u670d\u52a1")

        self.verticalLayout_5.addWidget(self.operate_tool_box)


        self.horizontalLayout_3.addWidget(self.operating_widget)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1109, 33))
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
        self.menu_import.addSeparator()
        self.menu_import.addAction(self.action_clear)
        self.menu_check.addAction(self.action_check_infos)
        self.menu.addAction(self.action_analysis_report)
        self.menu.addAction(self.action_set_analysis_path)
        self.menu_2.addAction(self.action_summon_report_for_current)
        self.menu_2.addAction(self.action_summon_selectMulti)
        self.menu_2.addAction(self.action_summon_report_for_all)
        self.menu_2.addAction(self.action_set_summon_path)
        self.menu_3.addAction(self.action_prev_image)
        self.menu_3.addAction(self.action_next_image)
        self.toolBar.addAction(self.action_import_images)
        self.toolBar.addAction(self.action_import_folder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_import_models)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_prev_image)
        self.toolBar.addAction(self.action_next_image)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_check_infos)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_clear)

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
        self.action_summon_report_for_current.setText(QCoreApplication.translate("MainWindow", u"\u4e3a\u5f53\u524d\u9009\u4e2d\u9879\u751f\u6210\u62a5\u544a", None))
        self.action_set_analysis_path.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u89e3\u6790\u751f\u6210\u6587\u4ef6\u5939\u8def\u5f84", None))
        self.action_set_summon_path.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u751f\u6210\u62a5\u544a\u8def\u5f84", None))
        self.action_import_folder.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6587\u4ef6\u5939", None))
        self.action_next_image.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20\u56fe\u50cf", None))
        self.action_prev_image.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20\u56fe\u50cf", None))
        self.action_summon_report_for_all.setText(QCoreApplication.translate("MainWindow", u"\u4e3a\u5217\u8868\u6240\u6709\u9879\u76ee\u751f\u6210\u62a5\u544a", None))
        self.action_summon_selectMulti.setText(QCoreApplication.translate("MainWindow", u" \u591a\u9009\u5217\u8868\u6587\u4ef6\u8fdb\u884c\u62a5\u544a\u751f\u6210", None))
        self.action_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.label_display.setText("")
        self.btn_load_model.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6a21\u578b", None))
        self.btn_load_image.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u56fe\u50cf", None))
        self.operate_tool_box.setItemText(self.operate_tool_box.indexOf(self.page), QCoreApplication.translate("MainWindow", u"\u524d\u7f6e\u52a0\u8f7d", None))
        self.label_analysis_report.setText(QCoreApplication.translate("MainWindow", u"\u62a5\u544a\u89e3\u6790\u5c0f\u7a0b\u5e8f\u4f4d\u7f6e: ", None))
        self.btn_set_analysis_path.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u89e3\u6790\u62a5\u544a\u7684\u751f\u6210\u4f4d\u7f6e", None))
        self.btn_analysis_report.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u62a5\u544a", None))
        self.operate_tool_box.setItemText(self.operate_tool_box.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"\u89e3\u6790\u7aef\u5c0f\u7a0b\u5e8f", None))
        self.label_report_path.setText(QCoreApplication.translate("MainWindow", u"\u62a5\u544a\u751f\u6210\u8def\u5f84\u4f4d\u4e8e: ", None))
        self.btn_set_summon_path.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e\u751f\u6210\u62a5\u544a\u8def\u5f84", None))
        self.btn_summon_report_for_current.setText(QCoreApplication.translate("MainWindow", u"\u4e3a\u5f53\u524d\u9009\u4e2d\u9879\u751f\u6210\u62a5\u544a", None))
        self.btn_summon_report_for_all.setText(QCoreApplication.translate("MainWindow", u"\u4e3a\u5217\u8868\u4e2d\u6240\u6709\u9879\u76ee\u751f\u6210\u62a5\u544a", None))
        self.btn_summon_select_multi.setText(QCoreApplication.translate("MainWindow", u"\u591a\u9009\u5217\u8868\u6587\u4ef6", None))
        self.operate_tool_box.setItemText(self.operate_tool_box.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"\u751f\u6210\u7aef\u5c0f\u7a0b\u5e8f", None))
        self.label_soundinfo.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u670d\u52a1\u7ed3\u679c\uff1a", None))
        self.btn_check_indications.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770b\u6307\u5f15...", None))
        self.btn_audio_control.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5f55\u97f3", None))
        self.operate_tool_box.setItemText(self.operate_tool_box.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u670d\u52a1", None))
        self.menu_import.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.menu_check.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u770b", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u89e3\u6790", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u822a", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

