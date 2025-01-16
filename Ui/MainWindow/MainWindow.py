import sys
from PySide6 import QtWidgets
from .ui_MainWindow import Ui_MainWindow
from loguru import logger


"""
    MainWindow is the Main Interactive Window work as the top level 
    interactive adapter with user and the applications
"""
class MainWindow(QtWidgets.QMainWindow):
    def __setup_logger(self):
        logger.add(sys.stdout, level="TRACE")

    """
        This is the initializations of the mainWindow
    """
    def __init__(self, parent = None):
        self.__setup_logger()
        logger.trace("entering initialize...")
        super().__init__(parent)
        # Setup Ui Form from Ui_MainWindow
        self.__Ui = Ui_MainWindow()
        self.__Ui.setupUi(self)

    """
        done after user quit
    """
    def finalize(self):
        # do the finalize when the exec is quited
        logger.trace("entering finalize...")
        logger.remove()





