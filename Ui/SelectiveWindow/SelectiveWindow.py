from . import Ui_SelectiveWindow
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QSizePolicy, QMainWindow, QLabel, \
    QCheckBox, QMessageBox, QAbstractItemView, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItem, QStandardItemModel, QPixmap
from Core.Common.path_utils import PathUtils
from loguru import logger

class SelectiveWindow(QMainWindow):
    onTellFetch = Signal()

    def __init__(self, image_lists: list[str], parent = None):
        super().__init__(parent)
        self.__Ui = Ui_SelectiveWindow()
        self.__Ui.setupUi(self)
        self.__on_load_each_sections(image_lists)
        self.__on_select_image: list[str] = []
        self.__Ui.tableView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.__cancelled = False
        self.__init_connections()

    def __init_connections(self):
        self.__Ui.btn_cancel.clicked.connect(self.do_cancel)
        self.__Ui.btn_ensure.clicked.connect(self.close)
        self.__Ui.action_select_all.triggered.connect(self.select_all)
        self.__Ui.action_select_unall.triggered.connect(self.select_unall)
        
    def show(self):
        self.clear_self()
        super().show()

    def select_all(self):
        for row in range(self.model.rowCount()):
            index = self.model.index(row, 1) 
            checkbox: QCheckBox = self.__Ui.tableView.indexWidget(index)  
            checkbox.setChecked(True)
    
    def select_unall(self):
        for row in range(self.model.rowCount()):
            index = self.model.index(row, 1)  
            checkbox: QCheckBox = self.__Ui.tableView.indexWidget(index)  
            checkbox.setChecked(False)

    def do_cancel(self):
        self.__cancelled = True
        self.close()

    def fetch_result(self):
        return self.__on_select_image

    def clear_self(self):
        self.__on_select_image.clear()

    def closeEvent(self, event):
        logger.trace("User shell close the processing window, check the case")
        if self.__cancelled:
            self.__cancelled = False
            self.clear_self()
            return
        self.__on_collect()
        if len(self.__on_select_image) == 0:
            self.clear_self()
            return
        images = ""
        for each in self.__on_select_image:
            images += each + "\n"
        reply = QMessageBox.question(self, '确定', f'请确定是这些图像！{images}',
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)   
        if reply == QMessageBox.Yes:
            self.onTellFetch.emit()
            event.accept()  
        else:
            event.ignore()  


    def __on_load_each_sections(self, image_lists: list[str]):
        self.model = QStandardItemModel(len(image_lists), 3) 
        self.model.setHorizontalHeaderLabels(["图像名称", "图像路径", "选择"])
        index = 0
        self.__Ui.tableView.setModel(self.model)
        for each in image_lists:
            self.__on_load_each_row(index, each)
            index += 1 

    def __on_collect(self):
        for row in range(self.model.rowCount()):
            index = self.model.index(row, 1) 
            checkbox: QCheckBox = self.__Ui.tableView.indexWidget(index)  
            if checkbox.isChecked():
                path_item = self.model.item(row, 2)
                path_value = path_item.text() 
                logger.trace(f"user add {path_value}")
                self.__on_select_image.append(path_value)


    def __on_load_each_row(self, row: int, path: str):
        self.model.setItem(row, 0, QStandardItem(PathUtils.gain_names_from_paths([path])[0]))
        self.model.setItem(row, 2, QStandardItem(path))
        checkbox = QCheckBox()
        self.__Ui.tableView.setIndexWidget(self.model.index(row, 1), checkbox)