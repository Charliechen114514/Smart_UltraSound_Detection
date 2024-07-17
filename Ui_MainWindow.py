# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1038, 690)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.imagesViewWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.imagesViewWidget.setObjectName("imagesViewWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.imagesViewWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileListsWidget = QtWidgets.QListWidget(parent=self.imagesViewWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileListsWidget.sizePolicy().hasHeightForWidth())
        self.fileListsWidget.setSizePolicy(sizePolicy)
        self.fileListsWidget.setMaximumSize(QtCore.QSize(150, 16777215))
        self.fileListsWidget.setObjectName("fileListsWidget")
        self.horizontalLayout.addWidget(self.fileListsWidget)
        self.imageframe = QtWidgets.QWidget(parent=self.imagesViewWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageframe.sizePolicy().hasHeightForWidth())
        self.imageframe.setSizePolicy(sizePolicy)
        self.imageframe.setObjectName("imageframe")
        self.gridLayout = QtWidgets.QGridLayout(self.imageframe)
        self.gridLayout.setObjectName("gridLayout")
        self.image_label = QtWidgets.QLabel(parent=self.imageframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setAutoFillBackground(True)
        self.image_label.setScaledContents(True)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.imageframe)
        self.horizontalLayout_3.addWidget(self.imagesViewWidget)
        self.toolsFrame = QtWidgets.QWidget(parent=self.centralwidget)
        self.toolsFrame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.toolsFrame.setObjectName("toolsFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.toolsFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.operatorBox = QtWidgets.QToolBox(parent=self.toolsFrame)
        self.operatorBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.operatorBox.setObjectName("operatorBox")
        self.imports = QtWidgets.QWidget()
        self.imports.setGeometry(QtCore.QRect(0, 0, 111, 142))
        self.imports.setObjectName("imports")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.imports)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.widget = QtWidgets.QWidget(parent=self.imports)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_load_pictures = QtWidgets.QPushButton(parent=self.widget)
        self.btn_load_pictures.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_load_pictures.setObjectName("btn_load_pictures")
        self.verticalLayout.addWidget(self.btn_load_pictures)
        self.btn_load_models = QtWidgets.QPushButton(parent=self.widget)
        self.btn_load_models.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_load_models.setObjectName("btn_load_models")
        self.verticalLayout.addWidget(self.btn_load_models)
        self.horizontalLayout_4.addWidget(self.widget)
        self.operatorBox.addItem(self.imports, "")
        self.recognize_page = QtWidgets.QWidget()
        self.recognize_page.setGeometry(QtCore.QRect(0, 0, 98, 68))
        self.recognize_page.setObjectName("recognize_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.recognize_page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_start_recognize = QtWidgets.QPushButton(parent=self.recognize_page)
        self.btn_start_recognize.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_start_recognize.setObjectName("btn_start_recognize")
        self.verticalLayout_2.addWidget(self.btn_start_recognize)
        self.operatorBox.addItem(self.recognize_page, "")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 182, 522))
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_2 = QtWidgets.QWidget(parent=self.page)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.audioGet_lineEdit = QtWidgets.QLineEdit(parent=self.widget_2)
        self.audioGet_lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.audioGet_lineEdit.setObjectName("audioGet_lineEdit")
        self.verticalLayout_3.addWidget(self.audioGet_lineEdit)
        self.btn_audioServer = QtWidgets.QPushButton(parent=self.widget_2)
        self.btn_audioServer.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_audioServer.setObjectName("btn_audioServer")
        self.verticalLayout_3.addWidget(self.btn_audioServer)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.operatorBox.addItem(self.page, "")
        self.horizontalLayout_2.addWidget(self.operatorBox)
        self.horizontalLayout_3.addWidget(self.toolsFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1038, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(parent=self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_select_model = QtGui.QAction(parent=MainWindow)
        self.action_select_model.setObjectName("action_select_model")
        self.action_load_images = QtGui.QAction(parent=MainWindow)
        self.action_load_images.setObjectName("action_load_images")
        self.action_showInfo = QtGui.QAction(parent=MainWindow)
        self.action_showInfo.setObjectName("action_showInfo")
        self.action_recognize_depatch = QtGui.QAction(parent=MainWindow)
        self.action_recognize_depatch.setObjectName("action_recognize_depatch")
        self.menu.addAction(self.action_select_model)
        self.menu.addAction(self.action_load_images)
        self.menu_3.addAction(self.action_showInfo)
        self.menu_4.addAction(self.action_recognize_depatch)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        self.operatorBox.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image_label.setText(_translate("MainWindow", "请导入图像"))
        self.btn_load_pictures.setText(_translate("MainWindow", "添加图片"))
        self.btn_load_models.setText(_translate("MainWindow", "添加模型"))
        self.operatorBox.setItemText(self.operatorBox.indexOf(self.imports), _translate("MainWindow", "导入"))
        self.btn_start_recognize.setText(_translate("MainWindow", "开始识别"))
        self.operatorBox.setItemText(self.operatorBox.indexOf(self.recognize_page), _translate("MainWindow", "开始识别"))
        self.audioGet_lineEdit.setText(_translate("MainWindow", "识别内容："))
        self.btn_audioServer.setText(_translate("MainWindow", "开始语音识别"))
        self.operatorBox.setItemText(self.operatorBox.indexOf(self.page), _translate("MainWindow", "语音识别"))
        self.menu.setTitle(_translate("MainWindow", "导入"))
        self.menu_2.setTitle(_translate("MainWindow", "查看"))
        self.menu_3.setTitle(_translate("MainWindow", "信息"))
        self.menu_4.setTitle(_translate("MainWindow", "开始识别"))
        self.action_select_model.setText(_translate("MainWindow", "加载模型文件"))
        self.action_load_images.setText(_translate("MainWindow", "导入图像"))
        self.action_showInfo.setText(_translate("MainWindow", "查看当前状态"))
        self.action_recognize_depatch.setText(_translate("MainWindow", "开始识别"))
