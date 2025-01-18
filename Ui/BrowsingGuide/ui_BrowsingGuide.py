# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BrowsingGuide.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_BrowsingGuide(object):
    def setupUi(self, BrowsingGuide):
        if not BrowsingGuide.objectName():
            BrowsingGuide.setObjectName(u"BrowsingGuide")
        BrowsingGuide.resize(199, 77)
        self.horizontalLayout = QHBoxLayout(BrowsingGuide)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(BrowsingGuide)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label = QLabel(BrowsingGuide)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)


        self.retranslateUi(BrowsingGuide)

        QMetaObject.connectSlotsByName(BrowsingGuide)
    # setupUi

    def retranslateUi(self, BrowsingGuide):
        BrowsingGuide.setWindowTitle(QCoreApplication.translate("BrowsingGuide", u"Form", None))
        self.label.setText(QCoreApplication.translate("BrowsingGuide", u"/", None))
    # retranslateUi

