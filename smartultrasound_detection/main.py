import sys
from PySide6 import QtWidgets
from Ui.MainWindow import MainWindow 
# Issuing for the global use of my classifier
from loguru import logger
from model_train.ModelUsing import Classifier
if __name__ == "__main__":
    logger.trace("creating application")
    app = QtWidgets.QApplication(sys.argv)
    logger.trace("creating application done")
    logger.trace("initializing mainwindow")
    main_window = MainWindow.MainWindow()
    logger.trace("initializing done")
    logger.trace("application show")
    main_window.show()
    res = app.exec()
    main_window.finalize()
    sys.exit(res)