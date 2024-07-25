from PyQt6.QtWidgets import QFileDialog
from Utils.Utils import Software_Utils

def is_valid(res: int):
    if res == 1:
        return "正常"
    else:
        return "异常"


class ReportGenerator:
    def __init__(self):
        self.after_ward_pic_paths = []
        self.after_ward_res = []
        self.report = ""

    def handle_raw_res(self, res, pic_raw_path):
        raw_res = res
        raw_pic_raw_path = pic_raw_path
        tmp_res = []
        for each_res, each_pic_path in zip(raw_res, raw_pic_raw_path):
            if Software_Utils.is_seperate_image(each_pic_path):
                self.after_ward_pic_paths.append(each_pic_path)
                self.after_ward_res.append(each_res)
            else:
                belonging_pic = Software_Utils.get_main_image_label(each_pic_path)

                if belonging_pic not in self.after_ward_pic_paths:
                    if len(self.after_ward_pic_paths) != 0:
                        if len(tmp_res) != 0:
                            prev_res = Software_Utils.get_main_res(tmp_res)
                            self.after_ward_res.append(prev_res)
                            tmp_res.clear()
                        else:
                            tmp_res.append(each_res)
                    self.after_ward_pic_paths.append(belonging_pic)
                    tmp_res.append(each_res)
        if len(tmp_res) != 0:
            prev_res = Software_Utils.get_main_res(tmp_res)
            self.after_ward_res.append(prev_res)

    def check_valid(self):
        if len(self.after_ward_res) != len(self.after_ward_pic_paths):
            return False, "没有确保结果和图片片路径对等！"
        return True, ""

    def generate_report(self):
        res = str()
        for each_res, each_pic_res in zip(self.after_ward_res, self.after_ward_pic_paths):
            res += "图片路径:> " + each_pic_res + "，其诊断结果为：" + is_valid(each_res) + "\n"
        self.report = res
        return res

    def show_for_file(self):
        path = QFileDialog.getSaveFileName(None, "输入保存文件名称", "")[0]
        if len(path) == 0:
            return
        with open(path, "w") as f:
            f.write(self.report)

    def make_all_clear(self):
        self.after_ward_pic_paths.clear()
        self.after_ward_res.clear()
