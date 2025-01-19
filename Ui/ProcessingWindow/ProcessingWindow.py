from . import Ui_ProcessingWindow
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Signal, Qt
from loguru import logger


class ProcessingWindow(QMainWindow):

    tellSummonReport = Signal()
    tellStopCurrentIssue = Signal()

    def __init__(self, parent = None):
        super().__init__(parent)
        self.__Ui = Ui_ProcessingWindow()
        self.__Ui.setupUi(self)
        self.__current_handling_tol = 0
        self.__current_handling_reco = 0
        self.__current_handling_summon = 0
        self.__pass_direct = False
        
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.__Ui.btn_continue_summon_report.clicked.connect(self.__on_tell_submit_the_report)

    @property
    def current_handling_tol(self):
        return self.__current_handling_tol

    @current_handling_tol.setter
    def current_handling_tol(self, size: int):
        self.__current_handling_tol = size
        self.__on_handling_tol_set_ui_flush()

    def set_handling_reco(self, index: int):
        self.current_handling_reco = index
    def set_handling_summon(self, index: int):
        self.current_handling_summon = index

    @property
    def current_handling_reco(self):
        return self.__current_handling_reco

    @current_handling_reco.setter
    def current_handling_reco(self, size: int):
        self.__current_handling_reco = size
        self.__on_handling_reco_set_ui_flush()

    @property
    def current_handling_summon(self):
        return self.__current_handling_summon

    @current_handling_summon.setter
    def current_handling_summon(self, size: int):
        self.__current_handling_summon = size
        self.__on_handling_summon_set_ui_flush()

    def show(self):
        self.__pass_direct = False
        logger.trace("window is shown")
        super().show()

# ------------- Private ------------------------
    def clear_self(self):
        self.__Ui.summon_progressBar.setValue(self.__current_handling_summon)
        self.__Ui.label_summon_show_left.setText(
            f"{self.__current_handling_summon} | {self.__current_handling_tol}")
        self.__Ui.recognize_progressBar.setValue(self.__current_handling_reco)
        self.__Ui.label_show_recognize_left.setText(
            f"{self.__current_handling_reco} | {self.__current_handling_tol}")
        self.__Ui.result_show.clear()
    
    def __on_handling_tol_set_ui_flush(self):
        logger.trace(f"set the tol: {self.__current_handling_tol}")
        self.__Ui.recognize_progressBar.setMaximum(self.__current_handling_tol)
        self.__Ui.label_show_recognize_left.setText(
            f"{self.__current_handling_reco} | {self.__current_handling_tol}")
        self.__Ui.summon_progressBar.setMaximum(self.__current_handling_tol)
        self.__Ui.label_summon_show_left.setText(
            f"{self.__current_handling_summon} | {self.__current_handling_tol}")

    def __on_handling_summon_set_ui_flush(self):
        logger.trace(f"set the summon: {self.__current_handling_summon}")
        self.__Ui.summon_progressBar.setValue(self.__current_handling_summon)
        self.__Ui.label_summon_show_left.setText(
            f"{self.__current_handling_summon} | {self.__current_handling_tol}")
        if self.current_handling_summon == self.current_handling_tol:
            self.__pass_direct = True

    def __on_handling_reco_set_ui_flush(self):
        logger.trace(f"set the reco: {self.__current_handling_reco}")
        self.__Ui.recognize_progressBar.setValue(self.__current_handling_reco)
        self.__Ui.label_show_recognize_left.setText(
            f"{self.__current_handling_reco} | {self.__current_handling_tol}")
        
    def onHandleTheReadynessOfSummon(self):
        logger.debug("on ready the summon!")
        self.__Ui.btn_continue_summon_report.setEnabled(
            self.__current_handling_reco == self.__current_handling_tol)

    def closeEvent(self, event):
        logger.trace("User shell close the processing window, check the case")
        if self.__pass_direct:
            event.accept()  
            self.clear_self()   
            return   
        reply = QMessageBox.question(self, '是否退出', '所有的工作进度都会丢失！',
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)   
        if reply == QMessageBox.Yes:
            self.tellStopCurrentIssue.emit()
            event.accept()  
        else:
            event.ignore()      

    def handle_report_summon_where(self, where: str):
        self.__Ui.result_show.append("此报告生成于: " + where)

    def handle_result(self, buf: str):
        self.__Ui.result_show.append(buf)

    def __on_tell_submit_the_report(self):
        self.tellSummonReport.emit() 