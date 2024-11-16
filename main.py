from PyQt6 import QtWidgets
import sys
import MainWindow
# To use prediction
from ModelUsing.MyModel import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    test_window = MainWindow.MainWindow()
    test_window.show()
    res = app.exec()
    test_window.do_finalize()
    sys.exit(res)

