# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectiveWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTableView, QToolBar, QWidget)

class Ui_SelectiveWindow(object):
    def setupUi(self, SelectiveWindow):
        if not SelectiveWindow.objectName():
            SelectiveWindow.setObjectName(u"SelectiveWindow")
        SelectiveWindow.resize(856, 577)
        self.action_select_all = QAction(SelectiveWindow)
        self.action_select_all.setObjectName(u"action_select_all")
        self.action_select_all.setMenuRole(QAction.MenuRole.NoRole)
        self.action_select_unall = QAction(SelectiveWindow)
        self.action_select_unall.setObjectName(u"action_select_unall")
        self.action_select_unall.setMenuRole(QAction.MenuRole.NoRole)
        self.centralwidget = QWidget(SelectiveWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.horizontalHeader().setHighlightSections(False)
        self.tableView.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_cancel = QPushButton(self.widget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.btn_cancel)

        self.btn_ensure = QPushButton(self.widget)
        self.btn_ensure.setObjectName(u"btn_ensure")
        self.btn_ensure.setMinimumSize(QSize(0, 50))

        self.horizontalLayout.addWidget(self.btn_ensure)


        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        SelectiveWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SelectiveWindow)
        self.statusbar.setObjectName(u"statusbar")
        SelectiveWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(SelectiveWindow)
        self.toolBar.setObjectName(u"toolBar")
        SelectiveWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.action_select_all)
        self.toolBar.addAction(self.action_select_unall)

        self.retranslateUi(SelectiveWindow)

        QMetaObject.connectSlotsByName(SelectiveWindow)
    # setupUi

    def retranslateUi(self, SelectiveWindow):
        SelectiveWindow.setWindowTitle(QCoreApplication.translate("SelectiveWindow", u"\u9009\u62e9\u8981\u751f\u6210\u7684\u6587\u4ef6", None))
        self.action_select_all.setText(QCoreApplication.translate("SelectiveWindow", u"\u5168\u9009", None))
        self.action_select_unall.setText(QCoreApplication.translate("SelectiveWindow", u"\u5168\u4e0d\u9009", None))
        self.btn_cancel.setText(QCoreApplication.translate("SelectiveWindow", u"\u53d6\u6d88", None))
        self.btn_ensure.setText(QCoreApplication.translate("SelectiveWindow", u"\u786e\u5b9a", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("SelectiveWindow", u"toolBar", None))
    # retranslateUi

