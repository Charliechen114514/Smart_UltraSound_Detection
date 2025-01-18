# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InfoWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QMainWindow,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_InfoWindow(object):
    def setupUi(self, InfoWindow):
        if not InfoWindow.objectName():
            InfoWindow.setObjectName(u"InfoWindow")
        InfoWindow.resize(449, 254)
        icon = QIcon()
        icon.addFile(u":/icons/window_icon/window_icon/check_infos.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        InfoWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(InfoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem13)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addWidget(self.widget)

        InfoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(InfoWindow)
        self.statusbar.setObjectName(u"statusbar")
        InfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InfoWindow)

        QMetaObject.connectSlotsByName(InfoWindow)
    # setupUi

    def retranslateUi(self, InfoWindow):
        InfoWindow.setWindowTitle(QCoreApplication.translate("InfoWindow", u"\u67e5\u8be2", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InfoWindow", u"\u53c2\u6570", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InfoWindow", u"\u8bf4\u660e", None));
        ___qtablewidgetitem2 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InfoWindow", u"\u56fe\u50cf\u5f20\u6570", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InfoWindow", u"\u6a21\u578b\u4f4d\u7f6e", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("InfoWindow", u"\u751f\u6210\u62a5\u544a\u8def\u5f84", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("InfoWindow", u"\u89e3\u6790\u62a5\u544a\u751f\u6210\u8def\u5f84", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("InfoWindow", u"0", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("InfoWindow", u"\u52a0\u8f7d\u7684\u56fe\u50cf\u5f20\u6570", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("InfoWindow", u"\u65e0", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("InfoWindow", u"\u52a0\u8f7d\u7684\u6a21\u578b\u4f4d\u7f6e", None));
        ___qtablewidgetitem10 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("InfoWindow", u"\u65e0", None));
        ___qtablewidgetitem11 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("InfoWindow", u"\u62a5\u544a\u7684\u751f\u6210\u6587\u4ef6\u5939\u6240\u5728\u5730", None));
        ___qtablewidgetitem12 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("InfoWindow", u"\u65e0", None));
        ___qtablewidgetitem13 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("InfoWindow", u"\u62a5\u544a\u7684\u751f\u6210\u6587\u4ef6\u5939\u6240\u5728\u5730", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

    # retranslateUi

