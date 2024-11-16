from PyQt6.QtWidgets import QFileDialog

from ReportGenerator.ReportGenerator_IMPL import ReportGenerator_Impl
from Utils.Utils import Software_Utils

def is_valid(res: int):
    if res == 1:
        return "正常"
    else:
        return "异常"


class ReportGenerator:
    LABEL_PREFIX = "当前报告生成路径: "
    LABEL_NO_PATH = "当前没有指定报告生成文件夹!"
    def __init__(self):
        self.__after_ward_pic_paths = []
        self.__after_ward_res = []
        self.__impl = ReportGenerator_Impl()

    def handle_raw_res(self, res, pic_raw_path):
        raw_res = res
        raw_pic_raw_path = pic_raw_path
        tmp_res = []
        for each_res, each_pic_path in zip(raw_res, raw_pic_raw_path):
            if Software_Utils.is_seperate_image(each_pic_path):
                self.__after_ward_pic_paths.append(each_pic_path)
                self.__after_ward_res.append(each_res)
            else:
                belonging_pic = Software_Utils.get_main_image_label(each_pic_path)

                if belonging_pic not in self.__after_ward_pic_paths:
                    if len(self.__after_ward_pic_paths) != 0:
                        if len(tmp_res) != 0:
                            prev_res = Software_Utils.get_main_res(tmp_res)
                            self.__after_ward_res.append(prev_res)
                            tmp_res.clear()
                        else:
                            tmp_res.append(each_res)
                    self.__after_ward_pic_paths.append(belonging_pic)
                    tmp_res.append(each_res)
        if len(tmp_res) != 0:
            prev_res = Software_Utils.get_main_res(tmp_res)
            self.__after_ward_res.append(prev_res)

    def check_valid(self):
        if len(self.__after_ward_res) != len(self.__after_ward_pic_paths):
            return False, "没有确保结果和图片片路径对等！"
        return True, ""

    def generate_indications(self):
        res = str()
        for each_res, each_pic_res in zip(self.__after_ward_res, self.__after_ward_pic_paths):
            res += "图片路径:> " + each_pic_res + "，其诊断结果为：" + is_valid(each_res) + "\n"
        return res

    def set_report_dir(self, path: str):
        self.__impl.set_generate_dir(path)

    def fetch_tell_report_dir_labelText(self) -> str:
        if self.__impl.get_generate_dir() == "":
            return ReportGenerator.LABEL_NO_PATH
        else:
            return ReportGenerator.LABEL_PREFIX + self.__impl.get_generate_dir()
    def fetch_report_dir(self) -> str:
        return self.__impl.get_generate_dir()
    def generate_report(self):
        pass

    def make_all_clear(self):
        self.__after_ward_pic_paths.clear()
        self.__after_ward_res.clear()
