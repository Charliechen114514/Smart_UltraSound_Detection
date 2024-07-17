from PyQt6.QtWidgets import QFileDialog


def is_valid(res: int):
    if res == 1:
        return "正常"
    else:
        return "异常"


class ReportGenerator:
    def __init__(self):
        self.raw_res = []
        self.raw_pic_path = []
        self.report = ""

    def set_res(self, res, pic_raw_path):
        self.raw_res = res
        self.raw_pic_path = pic_raw_path

    def check_valid(self):
        if len(self.raw_res) != len(self.raw_pic_path):
            return False, "没有确保结果和图片片路径对等！"
        return True, ""

    def generate_report(self):
        res = str()
        for each_res, each_pic_res in zip(self.raw_res, self.raw_pic_path):
            res += "图片路径:> " + each_pic_res + "，其诊断结果为：" + is_valid(each_res) + "\n"
        self.report = res
        return res

    def show_for_file(self):
        path = QFileDialog.getSaveFileName(None, "输入保存文件名称", "")[0]
        if len(path) == 0:
            return
        with open(path, "w") as f:
            f.write(self.report)

