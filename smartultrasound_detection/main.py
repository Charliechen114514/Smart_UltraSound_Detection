import sys
from PySide6 import QtWidgets
from Ui.MainWindow import MainWindow 
# Issuing for the global use of my classifier
from model_train.ModelUsing import Classifier
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow.MainWindow()
    main_window.show()
    res = app.exec()
    main_window.finalize()
    sys.exit(res)