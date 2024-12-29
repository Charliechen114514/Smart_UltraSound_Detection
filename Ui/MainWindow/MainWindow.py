from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, QFile, QMetaObject
from PySide6.QtWidgets import QFileDialog, QMessageBox, QApplication
from .ui_MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        # Setup Ui Form from Ui_MainWindow
        self.__Ui = Ui_MainWindow()
        self.__Ui.setupUi(self)

