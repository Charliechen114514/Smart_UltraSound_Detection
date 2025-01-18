from PySide6.QtWidgets import QWidget, QFileDialog
from Core.Common import ImageUtils
from Core.Common import ModelUtils

class UiUtils:
    @staticmethod
    def makeup_image_filters() -> str:
        return "图像文件 (" + " ".join([f"*{ext}" for ext in ImageUtils.supportive_image_extensions]) + ")"
    
    @staticmethod
    def makeup_model_filters() -> str:
        return "模型文件 (" + " ".join([f"*{ext}" for ext in ModelUtils.supportive_model_extensions]) + ")"

    @staticmethod
    def fetch_selected_dirent(parent: QWidget, caption: str, dirent = ".") -> str:
        return QFileDialog.getExistingDirectory(parent, caption, dirent)

    @staticmethod
    def fetch_selected_files(parent: QWidget, cap: str, dirent = ".", filters = makeup_image_filters()) -> list[str]:
        return QFileDialog.getOpenFileNames(parent, cap, dirent, filters)[0]

    @staticmethod
    def fetch_selected_file(parent: QWidget, cap: str, dirent = ".", filters = makeup_model_filters()) -> str:
        return QFileDialog.getOpenFileName(parent, cap, dirent, filters)[0]
    
    @staticmethod
    def fetch_open_dirent(parent: QWidget, cap: str, dirent = ".") -> str:
        return QFileDialog.getExistingDirectory(parent, cap, dirent)
