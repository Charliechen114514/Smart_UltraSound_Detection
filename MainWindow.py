from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt, QFile
from PyQt6.QtWidgets import QFileDialog, QMessageBox

import Ui_MainWindow

# Import the Components
from ImageBrowser.ImageBrowseUiManager import ImageBrowserUiManager
from Audio.AudioServerControl import AudioServer
from ModelController.ModelController import ModelController
from FileViewManager.FileViewManager import FileViewManager
from ModelUsing.ModelExecutor import ModelExecutor
from Utils.Utils import Software_Utils
from WaitingProcessBar.WaitingWidget import ReminderWindow
from ReportGenerator.ReportGenerator import ReportGenerator
from DetectWave.detectWave_BackEnd import ImageWavePraser
from ReportAnalysis.ReportAnalysis import ReportAnalysisHandler

control_modifier = Qt.KeyboardModifier.ControlModifier
shift_modifier = Qt.KeyboardModifier.ShiftModifier


class MainWindow(QtWidgets.QMainWindow):
    WINDOW_TITLE = "彩智快警——智慧彩超辅助系统"
    UI_STYLE_SHEET_PATH = "ui_resources/light/lightstyle.qss"

    def __init__(self, parent=None):
        # Do things here when init
        super().__init__(parent)
        self.audioServer = AudioServer(self)
        self.control_Audio_state = False
        self.reportGenerator = ReportGenerator()
        self.model_executor = None
        self.__UI = Ui_MainWindow.Ui_MainWindow()
        self.__UI.setupUi(self)
        self.waveDetector = ImageWavePraser()
        self.waveDetector.set_write_path("./runtime_middlewares/")
        Software_Utils.createDirentAnyway("./runtime_middlewares/")
        # Info the Image Browser Manager
        self.__image_manager = ImageBrowserUiManager(self.__UI.image_label)
        self.__model_manager = ModelController()
        self.__file_view_manager = FileViewManager(self.__UI.fileListsWidget)
        self.__analysis_image_report_handler = ReportAnalysisHandler()
        self.__init_connections()
        self.__load_base_ui()
        self.reminder_window = ReminderWindow()

    def __load_base_ui(self):
        # Window_Name
        self.setWindowTitle(MainWindow.WINDOW_TITLE)
        # Analysis report labels
        self.__UI.label_tell_save_anaysis_path.setText(self.__analysis_image_report_handler.get_current_label())
        # Qss
        self.__load_qss()

    def __load_qss(self):
        qss_pth = MainWindow.UI_STYLE_SHEET_PATH
        with open(qss_pth, 'r') as f:
            res = f.read()
        self.setStyleSheet(res)

    def __handle_image_browser_event(self, key: QtGui.QKeyEvent):
        if key.key() == Qt.Key.Key_Left:
            if not self.__check_and_reject_null_image_browser():
                return
            self.to_prev()
        elif key.key() == Qt.Key.Key_Right:
            if not self.__check_and_reject_null_image_browser():
                return
            self.to_next()

    def __handle_ui_show_event(self, key: QtGui.QKeyEvent):
        modifiers = key.modifiers()
        keys = key.key()
        # Ctrl + Shift + V
        if modifiers == control_modifier | shift_modifier and keys == Qt.Key.Key_V:
            self.__UI.operatorBox.setVisible(not self.__UI.operatorBox.isVisible())
        elif modifiers == control_modifier | shift_modifier and keys == Qt.Key.Key_M:
            self.__UI.fileListsWidget.setVisible(not self.__UI.fileListsWidget.isVisible())

    def __init_connections(self):
        # 初始化菜单栏链接
        self.__UI.action_load_images.triggered.connect(self.load_in_files)
        self.__UI.action_select_model.triggered.connect(self.load_model)
        self.__UI.action_showInfo.triggered.connect(self.show_current_state)
        self.__UI.action_recognize_depatch.triggered.connect(self.make_recognize)
        self.__UI.action_set_report_gen_path.triggered.connect(self.__handle_set_analysis_report_gen_path)
        self.__UI.action_start_gen_report_analysis.triggered.connect(self.handle_upload_report_image)

        # 初始化左侧文件栏控制链接
        self.__UI.fileListsWidget.itemClicked.connect(self.switch_to_by_file_name)

        # 初始化按钮行为
        self.__UI.btn_load_pictures.clicked.connect(self.load_in_files)
        self.__UI.btn_load_models.clicked.connect(self.load_model)
        self.__UI.btn_start_recognize.clicked.connect(self.make_recognize)
        self.__UI.btn_audioServer.clicked.connect(self.handle_audio_button_slot)
        self.__UI.btn_uploadReport.clicked.connect(self.handle_upload_report_image)
        self.__UI.btn_setTargetReport_GenPath.clicked.connect(self.__handle_set_analysis_report_gen_path)

        # 初始化组件
        self.audioServer.signal_tell_recognize.connect(self.handle_audio_result_slot)

    def __check_and_reject_null_image_browser(self):
        if self.__image_manager.get_current_size() == 0:
            QMessageBox.critical(self, "尚未导入图片！", "你需要在菜单栏中导入图片！")
            return False
        return True

    def __check_model_fine(self):
        model_path = self.__model_manager.get_cur_focus_model_name()
        if model_path == "":
            QMessageBox.critical(self, "尚未加载模型！", "请加载模型")
            return False
        if not QFile.exists(model_path):
            QMessageBox.critical(self, "尚未加载模型！", "检查模型路径: >" + model_path)
            return False
        return True

    def __switch_by_index(self, index: int):
        flag = self.__image_manager.jump(index)
        text = self.__image_manager.get_cur_description_text()
        self.setStatusTip(text)
        return flag

    def load_in_files(self):
        results = QFileDialog.getOpenFileNames(self, "选择想要加载的文件", "", self.__image_manager.get_suffix_logger())
        files = results[0]
        if len(files) == 0:
            return
        for file in files:
            self.__do_wave_detect(file)

    def switch_to_by_file_name(self):
        item = self.__UI.fileListsWidget.selectedItems()[0]
        file_name = item.text()
        index = self.__image_manager.get_index_by_file_name(file_name)
        if index == -1:
            QMessageBox.critical(self, "没找到！", "尚未找到目标文件，检查是否文件移动！")
            return
        self.__switch_by_index(index)

    def load_model(self):
        result = QFileDialog.getOpenFileName(self, "选择想要加载的文件", "", self.__model_manager.get_supported_model())
        if len(result[0]) == 0:
            return
        self.__model_manager.en_model_name(result[0])

    def to_next(self):
        if not self.__switch_by_index(self.__image_manager.get_current_focus_index() + 1):
            res = QMessageBox.question(self, "！", "当前已经到达最后一页！是否返回第一页？")
            if res == QMessageBox.StandardButton.Yes:
                self.__switch_by_index(0)

    def to_prev(self):
        if not self.__switch_by_index(self.__image_manager.get_current_focus_index() - 1):
            res = QMessageBox.question(self, "！", "当前已经到达第一页！是否返回最后一页？")
            if res == QMessageBox.StandardButton.Yes:
                # 查看最后一张
                self.__switch_by_index(self.__image_manager.get_current_size() - 1)

    def make_recognize(self):
        if not self.__check_model_fine():
            return
        if self.__image_manager.get_current_size() == 0:
            QMessageBox.critical(self, "导入图片", "请导入图片先")
            return
        self.reminder_window.set_total(self.__image_manager.get_current_size())
        self.model_executor = ModelExecutor(self.__model_manager.get_cur_focus_model_name(), self)
        self.reminder_window.init_connect(self.model_executor)
        self.model_executor.load_images_path_and_make_init(self.__image_manager.get_images_raw_file_name())
        faults, res = self.model_executor.make_predictions()
        if len(faults) != 0:
            QMessageBox(self, "发生图片加载错误", self.model_executor.make_inform_faults(faults))
            return
        self.reminder_window.show()
        self.reportGenerator.handle_raw_res(res, self.__image_manager.get_images_raw_file_name())
        is_valid, descriptions = self.reportGenerator.check_valid()
        if not is_valid:
            QMessageBox.critical(self, "发生错误", descriptions)
            return
        self.reminder_window.set_show_text(self.reportGenerator.generate_report())
        # self.reportGenerator.show_for_file()
        # self.reportGenerator.gen_doc_report("../src/1.docx", "./result/检测报告1.docx")
        # self.reportGenerator.gen_doc_report("../src/3.docx", "./result/检测报告3.docx")
        # self.reportGenerator.gen_doc_report("../src/17.docx", "./result/检测报告17.docx")
        # self.reportGenerator.gen_doc_report("../src/20.docx", "./result/检测报告20.docx")
        # self.reportGenerator.gen_doc_report("../src/36.docx", "./result/检测报告8.docx")
        # self.reportGenerator.gen_doc_report("../src/40.docx", "./result/检测报告12.docx")
        self.reportGenerator.make_all_clear()
        self.reminder_window.activateWindow()

    def show_current_state(self):
        pic_size = self.__image_manager.get_current_size()
        cur_pic_info = self.__image_manager.get_cur_description_text()
        model_path = self.__model_manager.get_cur_focus_model_name()
        if pic_size == 0:
            pics_info = "当前没有图片！\n"
        else:
            pics_info = cur_pic_info + "\n"
        if model_path == "":
            model_info = "当前没有加载任何模型！\n"
        else:
            model_info = "模型路径为:\n" + model_path + "\n"

        QMessageBox.information(self, "当前状态", pics_info + model_info)
        return

    def keyPressEvent(self, key_env: QtGui.QKeyEvent):
        self.__handle_image_browser_event(key_env)
        self.__handle_ui_show_event(key_env)

    def handle_audio_button_slot(self):
        self.control_Audio_state = not self.control_Audio_state
        if self.control_Audio_state:
            self.audioServer.start_recording()
            self.__UI.btn_audioServer.setText("结束语音识别")
        else:
            self.audioServer.stop_recording()
            self.__UI.btn_audioServer.setText("开始语音识别")

    def __do_wave_detect(self, file: str):
        self.waveDetector.set_file_name(Software_Utils.get_file_name_accord_path(file))
        self.waveDetector.analysis_image(file)
        res_of_file = self.waveDetector.get_init_paths()
        if len(res_of_file) == 0:
            QMessageBox.critical(self, "分析异常", "图像:> " + file + "没有办法检测到单个波形！采用全局分析")
            res = list()
            res.append(file)
            state, failed = self.__image_manager.push_back_paths(res)
        else:
            state, failed = self.__image_manager.push_back_paths(res_of_file)
        if not state:
            for each_failed in failed:
                QMessageBox.critical(self, "出错了！", "抱歉！无法加载路径：" + each_failed + "!")
        self.waveDetector.clear_res()
        self.__switch_by_index(self.__image_manager.get_current_size() - 1)
        self.__file_view_manager.flush_file_names(self.__image_manager.get_images_file_name())

    def handle_audio_result_slot(self, result: str):
        self.__UI.audioGet_lineEdit.setText("识别内容: " + result)

    def handle_upload_report_image(self):
        res, reason = self.__analysis_image_report_handler.get_is_analysis_ready()
        if res is False:
            QMessageBox.critical(self, "注意", reason)
            return

        path = Software_Utils.get_current_support_existing_image_path(self, "选择目标导入报告图象")
        if path is None:
            return
        self.__analysis_image_report_handler.set_current_handling_image(path)
        self.__analysis_image_report_handler.debug_set_src_report_path("../src/001_解析报告.docx")
        res, reason = self.__analysis_image_report_handler.analysis_report()
        if res:
            QMessageBox.information(self, "解析成功", "图象解析成功，请到:\n"
                                    + self.__analysis_image_report_handler.get_analysis_report_result_path()
                                    + "\n下查看")
        else:
            QMessageBox.critical(self, "解析失败", reason)

    def __handle_set_analysis_report_gen_path(self):
        path = Software_Utils.get_existing_dir(self, "选择目标文件夹")
        if path is None:
            return
        self.__analysis_image_report_handler.set_target_generate_path(path)
        self.__UI.label_tell_save_anaysis_path.setText(self.__analysis_image_report_handler.get_current_label())
