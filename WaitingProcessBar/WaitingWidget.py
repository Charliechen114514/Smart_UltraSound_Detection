from PyQt6.QtWidgets import QWidget
import reminderprocesswindow
from ModelUsing.ModelExecutor import ModelExecutor
class ReminderWindow(QWidget):
    def __init__(self, parent=None):
        # Do things here when init
        super().__init__(parent)
        self.__UI = reminderprocesswindow.Ui_ReminderProcessWindow()
        self.__UI.setupUi(self)
        self.cur = 0
        self.total = 0
        # 设置进度条的范围
        self.__UI.exportProgressBar.setMinimum(0)
        self.__UI.exportProgressBar.setStyleSheet(
            "QProgressBar { border: 2px solid grey; "
            "border-radius: 5px; background-color: #FFFFFF; "
            "text-align: center;}"
            "QProgressBar::chunk {background:QLinearGradient(x1:0,y1:0,x2:2,y2:0,stop:0 #666699,stop:1  #DB7093); }")

    def set_total(self, size: int):
        self.total = size
        self.__UI.exportProgressBar.setMaximum(size)

    def init_connect(self, model_executor: ModelExecutor):
        model_executor.finish_x.connect(self.handle_x)
        model_executor.finish_all.connect(self.handle_finish)

    def handle_finish(self):
        self.__UI.exportProgressBar.setValue(self.total)
        self.__UI.exportProcessTextEdit.setText("完成！")

    def handle_x(self, index: int):
        self.__UI.exportProcessTextEdit.setText("完成识别第" + str(index) + "张图片")
        self.__UI.exportProgressBar.setValue(index)

    def set_show_text(self, strings: str):
        self.__UI.sthFunShow.setText(strings)
