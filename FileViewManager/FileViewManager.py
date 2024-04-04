from PyQt6.QtWidgets import QListWidget, QListWidgetItem

class FileViewManager:
    def __init__(self, wid: QListWidget):
        self.__handlesWidget = wid
        self.file_names = []

    def flush_file_names(self, files: list[str]):
        self.file_names = files
        self.__handlesWidget.clear()
        for each in self.file_names:
            res = QListWidgetItem(self.__handlesWidget)
            res.setText(each)


