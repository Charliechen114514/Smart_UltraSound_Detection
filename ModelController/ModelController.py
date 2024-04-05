from PyQt6.QtCore import QFile


def is_accessible_model_path(model_name: str):
    return QFile.exists(model_name)


class ModelController:
    def __init__(self):
        self.__model = ""
        self.__model_lists = []
        self.__limit_suffix = ["pt"]

    def __is_right_file_format(self, model_name: str):
        for each_suffix in self.__limit_suffix:
            if model_name.endswith(each_suffix):
                return True

        return False

    def __check_index_valid(self, index: int):
        return 0 <= index < len(self.__model_lists)

    def __update_cur_model_file_name(self, index: int):
        if not self.__check_index_valid(index):
            return False
        self.__model = self.__model_lists[index]
        return True

    def get_supported_model(self):
        res = str()
        for each in self.__limit_suffix:
            res += each + "文件(*." + each + ");;"
        res = res.removesuffix(";;")
        return res

    def en_model_name(self, model_name: str):
        if not is_accessible_model_path(model_name):
            return False
        if not self.__is_right_file_format(model_name):
            return False

        self.__model_lists.append(model_name)
        self.__update_cur_model_file_name(len(self.__model_lists) - 1)

    def get_cur_focus_model_name(self):
        return self.__model

    def get_index_model(self, index: int):
        if not self.__check_index_valid(index):
            return ""
        return self.__model_lists[index]

    def de_model(self, index: int):
        if not self.__check_index_valid(index):
            return False
        self.__model_lists.pop(index)
        return True

    def get_cur_model_count(self):
        return len(self.__model_lists)
