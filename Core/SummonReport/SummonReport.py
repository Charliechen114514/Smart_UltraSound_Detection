from Core.OCR.FetchParamDriver import FetchParamDriver
from Core.SummonReport.ReportGeneratorCoreWrapper import ReportGeneratorIMPL
from Core.SummonReport.PossibleAdviceGenerator import SuggestionsFetcher
from Core.Common.path_utils import PathUtils
from loguru import logger

class SummonReportHandler:
    def __init__(self):
        self.__summon_folder = ""
        self.__param_fetcher = FetchParamDriver()

    @property
    def summon_folder(self):
        return self.__summon_folder
    
    @summon_folder.setter
    def summon_folder(self, path: str):
        self.__summon_folder = path    

    def summon_report(self, image_path:str, req_advice: bool) -> str:
        infos = self.__param_fetcher.fetch_params(image_path)
        logger.trace("infos are gathering at here: " + str(infos))
        gen_report_impl = ReportGeneratorIMPL()
        gen_report_impl.is_normal = req_advice
        gen_report_impl \
            .set_infoLists(infos)\
            .set_image_path(image_path)\
            .set_saving_path(
                self.__summon_folder, \
                PathUtils.gain_names_from_paths([image_path])[0])
        if req_advice:
            gen_report_impl.set_suggestions(SuggestionsFetcher.get_advice(infos, True))
        else:
            gen_report_impl.set_suggestions("无明显异常情况。")
        gen_report_impl.generate_document()
        self.__param_fetcher.clear_previous()
        return gen_report_impl.saving_path()
