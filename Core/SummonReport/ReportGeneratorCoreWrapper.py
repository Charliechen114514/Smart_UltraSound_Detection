from Core.SummonReport.ReportDocxGeneratorDriver import ReportDocxGeneratorCore
import os.path as pth


class ReportGeneratorIMPL:
    MIDDLE_NAME = "检测报告"

    def __init__(self):
        self.__infoLists = []
        self.__saving_path = ""
        self.is_normal = True
        self.__image_path = ""
        self.__suggestions = ""

    def set_saving_path(self, _dir: str, pic_file_name: str):
        self.__saving_path = pth.join(_dir, ReportGeneratorIMPL.MIDDLE_NAME + pic_file_name + ".docx")
        return self

    def saving_path(self):
        return self.__saving_path

    def set_image_path(self, path: str):
        self.__image_path = path
        return self

    def set_infoLists(self, infos: list[float]):
        self.__infoLists = infos
        return self

    def set_suggestions(self, sug: str):
        self.__suggestions = sug
        return self

    def generate_document(self):
        document = ReportDocxGeneratorCore()
        document.set_path(self.__saving_path)
        para = document.gain_blank_para()
        document.add_heading("_____医院\n", 1, True, para)
        document.add_heading("产科超声检查报告单", 3, True, para)
        run = document.draw_infos(para)
        document.insert_pic(self.__image_path, run, para)
        document.draw_table(self.__infoLists)
        para = document.gain_blank_para()
        suggestions = ""
        suggestions = self.__suggestions
        document.append_paragraph(para, "智能诊断意见：\n    {}\n".format(suggestions))
        document.append_paragraph(para, "超声所见：\n\n\n")
        document.append_paragraph(para, "超声提示：")

        document.draw_fin(para)
        document.save_this()
