from OCR.FetchParamDriver import FetchParamDriver
from .ReportGeneratorCoreWrapper import ReportGeneratorIMPL
from Utils.Utils import Software_Utils
from ReportGenerator.PossibleAdviceGenerator import SuggestionsFetcher

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
        self.__param_fetcher = FetchParamDriver()
        self.__generate_dir = ""
        self.__image_holding_path = ""
        self.__report_state = True

    def set_report_status(self, st: bool):
        self.__report_state = st
        return self

    def set_image_holding(self, path: str):
        self.__image_holding_path = path
        return self

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
        res = str("检测结果如下: \n")
        for each_res, each_pic_res in zip(self.__after_ward_res, self.__after_ward_pic_paths):
            res += "图片路径:> " + each_pic_res + "，其诊断结果为：" + is_valid(each_res) + "\n"
        return res + "\n"

    def gain_result(self):
        return zip(self.__after_ward_res, self.__after_ward_pic_paths)

    def set_report_dir(self, path: str):
        self.__generate_dir = path
        return self

    def fetch_tell_report_dir_labelText(self) -> str:
        if self.__generate_dir == "":
            return ReportGenerator.LABEL_NO_PATH
        else:
            return ReportGenerator.LABEL_PREFIX + self.__generate_dir

    def fetch_report_dir(self) -> str:
        return self.__generate_dir

    def generate_report(self):
        infos = self.__param_fetcher.fetch_params(self.__image_holding_path)
        print("infos are gathering at here: " + str(infos))
        gen_report_impl = ReportGeneratorIMPL()
        gen_report_impl.is_normal = self.__report_state
        (gen_report_impl
         .set_infoLists(infos)
         .set_image_path(self.__image_holding_path)
         .set_saving_path(self.__generate_dir,
                          Software_Utils.get_file_name_accord_path(
                              self.__image_holding_path)))
        if not self.__report_state:
            gen_report_impl.set_suggestions(SuggestionsFetcher.get_advice(infos, True))
        else:
            gen_report_impl.set_suggestions("无明显异常情况。")
        gen_report_impl.generate_document()
        self.__param_fetcher.clear_previous()

    def make_all_clear(self):
        self.__after_ward_pic_paths.clear()
        self.__after_ward_res.clear()
