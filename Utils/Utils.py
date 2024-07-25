from PyQt6.QtCore import QFileInfo, QDir


class Software_Utils:
    @staticmethod
    def get_file_name_accord_path(path: str):
        f = QFileInfo(path)
        return f.baseName()

    @staticmethod
    def get_full_file_name(path: str):
        f = QFileInfo(path)
        return f.fileName()

    @staticmethod
    def get_file_suffix_accord_path(path: str):
        f = QFileInfo(path)
        return f.suffix()

    @staticmethod
    def createDirentAnyway(path: str):
        dirent = QDir(path)
        if not dirent.exists():
            dirent.mkpath(".")

    @staticmethod
    def is_seperate_image(path: str):
        return Software_Utils.get_full_file_name(path).count("-") == 0
    @staticmethod
    def get_main_image_label(path: str):
        filename = Software_Utils.get_file_name_accord_path(path)
        main_name = filename.split("-")[0]
        suffix = Software_Utils.get_file_suffix_accord_path(path)
        return main_name + "." + suffix

    @staticmethod
    def get_main_res(res: list[int]):
        normal_cnt = 0
        abnormal_cnt = 0
        for each in res:
            if each == 1:
                normal_cnt += 1
            else:
                abnormal_cnt += 1
        if normal_cnt >= abnormal_cnt:
            return 1
        else:
            return 0
