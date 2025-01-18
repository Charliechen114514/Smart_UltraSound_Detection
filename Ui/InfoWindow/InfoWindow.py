from . import Ui_InfoWindow
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
from Core.InfoPackage import InfoPackage

class InfoWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.__UI = Ui_InfoWindow()
        self.__UI.setupUi(self)

    def setInfo(self, package: InfoPackage):
        self.__UI.tableWidget.setItem(1, 0, QTableWidgetItem(str(package.image_info)))
        self.__UI.tableWidget.setItem(1, 1, QTableWidgetItem(str(package.model_info)))
        self.__UI.tableWidget.setItem(1, 2, QTableWidgetItem(str(package.analysis_package)))
        self.__UI.tableWidget.setItem(1, 3, QTableWidgetItem(str(package.summon_package)))
        self.__UI.tableWidget.resizeColumnsToContents()

