from Core.OCR.ImageOCR import OCRTextCore
from Core.AnalysisReport.DocxGeneraterImpl import DocxGenerator_IMPL
from Core.AnalysisReport.ReportAnalysisCore import ReportAnalysisCore
import os

class NoneImageException(Exception):
    def __str__(self):
        return "Image is empty"

class AnalysisReportHandler:
    def __init__(self):
        self.__analysis_folder = ""
        self.__handling_report_image = ""

    @property
    def handling_image_report(self):
        return self.__handling_report_image
    
    @handling_image_report.setter
    def handling_image_report(self, path: str):
        self.__handling_report_image = path    

    @property
    def analysis_folder(self):
        return self.__analysis_folder
    
    @analysis_folder.setter
    def analysis_folder(self, path: str):
        self.__analysis_folder = path

    def gain_gen_path(self) -> str:
        return os.path.join(self.__analysis_folder, self.__handling_report_image)

    def analysis_report(self):
        if self.__handling_report_image == "":
            raise NoneImageException()
        strings = OCRTextCore.get_text_from_image_for_params(\
            self.__handling_report_image)['text'].strip().replace(",", ".").replace(" ", "")
        docx_impl = DocxGenerator_IMPL(strings)
        docx_impl.set_path(self.gain_gen_path())
        docx_impl.set_advice(strings)
        docx_impl.create_docx_sources()
        try:
            docx_impl.save_docx()
        except Exception as e:
            raise e