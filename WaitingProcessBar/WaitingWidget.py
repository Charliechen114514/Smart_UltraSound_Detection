from PyQt6.QtWidgets import QWidget
import reminderprocesswindow
from ModelUsing.ModelExecutor import ModelExecutor


class ReminderWindow(QWidget):
    def __init__(self, parent=None):
        # Do things here when init
        super().__init__(parent)
        self.__UI = reminderprocesswindow.Ui_ReminderProcessWindow()
        self.__UI.setupUi(self)
        self.setWindowTitle("结果浏览")
        self.cur = 0
        self.total = 0
        # 设置进度条的范围
        self.__UI.exportProgressBar.setMinimum(0)

    def closeEvent(self, a0):
        print("Close the dialog")
        self.clear_show()


    def set_total(self, size: int):
        self.total = size
        self.__UI.exportProgressBar.setMaximum(size)

    def handle_finish(self):
        self.__UI.exportProgressBar.setValue(self.total)
        self.__UI.exportProcessTextEdit.setText("完成！")

    def handle_x(self, index: int):
        self.__UI.exportProcessTextEdit.setText("完成识别第" + str(index) + "张图片")
        self.__UI.exportProgressBar.setValue(index)
        print("{}, {}".format(index, self.total))

    def set_show_text(self, strings: str):
        self.__UI.sthFunShow.setText(strings)

    def append_text(self, text: str):
        self.__UI.sthFunShow.append(text)
        self.__UI.sthFunShow.verticalScrollBar().setSliderPosition(
            self.__UI.sthFunShow.verticalScrollBar().maximum())

    def clear_show(self):
        self.__UI.sthFunShow.clear()