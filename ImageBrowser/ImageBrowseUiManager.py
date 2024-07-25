import os.path

from PyQt6.QtCore import QFile
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap, QImage
from ImageBrowser.ImageBrowserCore import ImageBrowseCore


def check_image_validity(image: QImage):
    return not QImage.isNull(image)


class ImageBrowserUiManager:
    def __init__(self, label: QLabel):
        self.__core = ImageBrowseCore()
        self.__handling_label = label
        self.__suffix_controller = ['jpg', 'png', 'jpeg']

    def get_suffix_logger(self):
        res = str()
        for each in self.__suffix_controller:
            res += each + "文件(" + "*." + each + ");;"
        res = res.removesuffix(";;")
        return res

    def __handles_en_images(self, paths: list[str]):
        return self.__core.en_image_paths(paths)

    def __handles_en_image(self, path: str):
        return self.__core.en_image_path(path)

    def __remove_image(self, index: int):
        return self.__core.de_image_list(index)

    def __get_image(self, index: int):
        # Cores Offset only change by this Application InterFaces
        return self.__core.visit_at(index)

    def push_back_path(self, path: str):
        # Never Allow None Path enters the lists
        if not QFile.exists(path):
            return False
        self.__handles_en_image(path)

    def push_back_paths(self, paths: list[str]):
        # Never Allow None Path enters the lists
        failed = []
        flags = True
        for path in paths:
            if not QFile.exists(path):
                failed.append(path)
                flags = False
                continue
            self.__handles_en_image(path)
        return flags, failed

    def insert_path(self, path: str, index: int):
        if self.__core.insert(path, index):
            return self.set_image(index)
        else: # Index Invalid
            return False

    def remove_image_by_index(self, index: int):
        return self.__remove_image(index)

    def remove_image_by_path_full(self, path: str):
        index = self.__core.get_offset(path)
        if index == -1:
            return False
        else:
            return self.__remove_image(index)

    def get_current_size(self):
        return self.__core.get_cur_size()

    def get_current_focus_index(self):
        return self.__core.get_cur_index()

    def set_image(self, index: int):
        # Will update Index
        res = self.__get_image(index)
        if not check_image_validity(res):
            return False
        self.__handling_label.setPixmap(QPixmap(res).scaled(self.__handling_label.size()))
        return True

    def view_next(self):
        return self.jump(self.get_current_focus_index() + 1)

    def view_prev(self):
        return self.jump(self.get_current_focus_index() - 1)

    def jump(self, index: int):
        if 0 <= index < self.get_current_size():
            return self.set_image(index)
        else:
            return False

    def get_images_file_name(self):
        images = self.__core.get_images_lists()
        res = []
        for image in images:
            res.append(os.path.basename(image))
        return res

    def get_images_raw_file_name(self):
        return self.__core.get_images_lists()

    def get_index_by_file_name(self, file_name: str):
        return self.__core.get_index_by_file_name(file_name)

    def get_cur_description_text(self):
        if self.__core.get_cur_size() == 0:
            return ""
        else:
            return \
                "当前你正在浏览第" + str(self.get_current_focus_index() + 1) + "张图片，共: " + \
                str(self.__core.get_cur_size()) + "张\n" + "图像地址: " + \
                self.__core.get_images_lists()[self.get_current_focus_index()] + "\n"
