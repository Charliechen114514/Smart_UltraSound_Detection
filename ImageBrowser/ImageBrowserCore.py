from PyQt6.QtGui import QImage


class ImageBrowseCore:
    def __init__(self):
        self.__imageList: list[str] = []
        self.__index = -1

    def get_images_lists(self):
        return self.__imageList

    def __check_index_valid(self, index: int):
        return 0 <= index < len(self.__imageList)

    def update_index(self, index: int):
        if not self.__check_index_valid(index):
            return False
        self.__index = index
        return True

    def get_cur_index(self):
        return self.__index

    def en_image_path(self, image_path: str):
        if self.__imageList.count(image_path) != 0:
            self.__imageList.pop(self.__imageList.index(image_path))
        self.__imageList.append(image_path)

    def en_image_paths(self, image_paths: list[str]):
        for each in image_paths:
            self.__imageList.append(each)

    def insert(self, image_path: str, index: int):
        if not self.__check_index_valid(index):
            return False
        self.__imageList.insert(index, image_path)
        return True

    def visit_at(self, index: int):
        if not self.__check_index_valid(index):
            return QImage()
        self.update_index(index)
        return QImage(self.__imageList[index])

    def get_path(self, index):
        if not self.__check_index_valid(index):
            return ""
        return self.__imageList[index]

    def get_offset(self, path: str):
        cur_find = 0
        for each in self.__imageList:
            if each == path:
                return cur_find
            cur_find += 1
        return -1

    def de_image_list(self, index: int):
        if not self.__check_index_valid(index):
            return False
        self.__imageList.pop(index)

    def de_image_list_by_path(self, path: str):
        self.__imageList.remove(path)

    def clear(self):
        self.update_index(-1)
        self.__imageList.clear()

    def get_cur_size(self):
        return len(self.__imageList)

    def get_index_by_file_name(self, name: str):
        for each in self.__imageList:
            if each.endswith(name):
                return self.__imageList.index(each)
        return -1