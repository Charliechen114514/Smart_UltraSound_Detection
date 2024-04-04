from PyQt6 import QtWidgets, QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFileDialog, QMessageBox
import Ui_MainWindow
from ImageBrowser.ImageBrowseUiManager import ImageBrowserUiManager
from ModelController.ModelController import ModelController
from FileViewManager.FileViewManager import FileViewManager

control_modifier = Qt.KeyboardModifier.ControlModifier
shift_modifier = Qt.KeyboardModifier.ShiftModifier


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        # Do things here when init
        super().__init__(parent)
        self.__UI = Ui_MainWindow.Ui_MainWindow()
        self.__UI.setupUi(self)
        # Info the Image Browser Manager
        self.__image_manager = ImageBrowserUiManager(self.__UI.image_label)
        self.__model_manager = ModelController()
        self.__file_view_manager = FileViewManager(self.__UI.fileListsWidget)
        self.__init_connections()
        self.__load_base_ui()

    def __load_base_ui(self):
        # Window_Name
        self.setWindowTitle("Model_Using_Interface")
        # Qss
        self.__load_qss()

    def __load_qss(self):
        qss_pth = "ui_resources/light/lightstyle.qss"
        res = str()
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
        self.__UI.action_load_images.triggered.connect(self.load_in_files)
        self.__UI.action_select_model.triggered.connect(self.load_model)
        self.__UI.fileListsWidget.itemClicked.connect(self.switch_to_by_file_name)

    def __check_and_reject_null_image_browser(self):
        if self.__image_manager.get_current_size() == 0:
            QMessageBox.critical(self, "尚未导入图片！", "你需要在菜单栏中导入图片！")
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
        state, failed = self.__image_manager.push_back_paths(files)
        if not state:
            for each_failed in failed:
                QMessageBox.critical(self, "出错了！", "抱歉！无法加载路径：" + each_failed + "!")
        self.__switch_by_index(self.__image_manager.get_current_size() - 1)
        self.__file_view_manager.flush_file_names(self.__image_manager.get_images_file_name())
        return

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
        if len(result[0]):
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

    def keyPressEvent(self, key_env: QtGui.QKeyEvent):
        self.__handle_image_browser_event(key_env)
        self.__handle_ui_show_event(key_env)
