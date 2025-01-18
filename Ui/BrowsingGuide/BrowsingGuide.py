from . import Ui_BrowsingGuide
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtCore import Signal

class BrowsingGuide(QWidget):
    """ define private signals """
    # When the return press is entered, index is posted
    postIndex = Signal(int)

    def __init__(self, parent = None):
        super().__init__(parent)
        self.__Ui = Ui_BrowsingGuide()
        self.__Ui.setupUi(self)
        self.reset_as_clean()
        self.__init_connections()
    
    def reset_as_clean(self):
        self.__size = 0
        self.__saved_index = -1
        self.__Ui.label.setText("")
        self.__Ui.lineEdit.setText("")
        self.__Ui.lineEdit.setEnabled(False)

    def set_totol_size(self, size: int):
        self.__Ui.lineEdit.setEnabled(True)
        self.__size = size
        self.__Ui.label.setText(f"/{self.__size}")

    def on_handle_textEdit(self):
        try:
            int_val = int(self.__Ui.lineEdit.text())
        except ValueError:
            self.__Ui.lineEdit.setText(str(self.__saved_index))
            QMessageBox.critical(self, "发生错误", "不是一个合法的数字")
            return
        if int_val <= 0 or int_val > self.__size:
            self.__Ui.lineEdit.setText(str(self.__saved_index))
            QMessageBox.critical(self, "发生错误", "超出范围！")
            return
        self.__saved_index = int_val - 1
        self.postIndex.emit(self.__saved_index)

    def __init_connections(self):
        self.__Ui.lineEdit.returnPressed.connect(self.on_handle_textEdit)