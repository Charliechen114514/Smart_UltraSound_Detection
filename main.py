from PyQt6 import QtWidgets
import sys
import MainWindow
app = QtWidgets.QApplication(sys.argv)
test_window = MainWindow.MainWindow()
test_window.show()
sys.exit(app.exec())
