from OCR.ImageOCR import OCRTextCore
from ReportAnalysis.DocxGeneraterImpl import DocxGenerator_IMPL
from ReportAnalysis.ReportAnalysisCore import ReportAnalysisCore
from Utils.Utils import Software_Utils

class ReportAnalysisHandler:
    SAVE_PATH_LABEL_NOT_EXIST_PREFIX = "当前未指定生成文件夹位置"
    SAVE_PATH_LABEL_PREFIX = "解析报告生成文件夹在:\n"

    def __init__(self):
        self.__report_path = ""
        self.__image_path = ""
        self.__target_gen_path = ""
        pass

    def get_is_analysis_ready(self) -> [bool, str]:
        if self.__target_gen_path == "":
            return False, "无对应保存地址，请先设置！"
        return True, ""

    def set_current_handling_image(self, path: str):
        self.__image_path = path

    def set_target_generate_path(self, path: str):
        self.__target_gen_path = path

    def get_current_label(self) -> str:
        if self.__target_gen_path == "":
            return ReportAnalysisHandler.SAVE_PATH_LABEL_NOT_EXIST_PREFIX
        else:
            return ReportAnalysisHandler.SAVE_PATH_LABEL_PREFIX + self.__target_gen_path

    def get_analysis_report_result_path(self) -> str:
        return self.__target_gen_path

    def gain_name_according_image(self) -> str:
        return self.__target_gen_path + "/" + Software_Utils.get_file_name_accord_path(self.__image_path) + "_解析报告.docx"

    def analysis_report(self) -> [bool, str]:
        # Software_Utils.copy_file(self.__report_path, self.__target_gen_path)
        strings = OCRTextCore.get_text_from_image_for_params(self.__image_path)['text'].strip().replace(",", ".").replace(" ", "")
        docx_impl = DocxGenerator_IMPL(strings)
        docx_impl.set_path(self.gain_name_according_image())
        docx_impl.set_advice(OCRTextCore.get_text_from_image_for_suggestions(
            self.__image_path)['text'].strip().replace(",", ".").replace(" ", ""))
        docx_impl.create_docx_sources()
        try:
            docx_impl.save_docx()
        except Exception as e:
            raise e
        return True, ""
