class ImageInfo:
    def __init__(self):
        self._image_size = 0
  
    @property
    def image_size(self):
        return self._image_size

    @image_size.setter
    def image_size(self, size: int):
        self._image_size = size

    def __str__(self):
        if self._image_size == 0:
            return "当前没有加载图像"
        return f"当前加载了{self._image_size}图像"

class ModelInfo:
    def __init__(self):
        self._model_path = ""
    
    @property
    def model_path(self):
        return self._model_path
    
    @model_path.setter
    def model_path(self, path: str):
        self._model_path = path

    def __str__(self):
        if self._model_path == "":
            return "当前没有加载模型"
        return f"当前加载模型路径: {self._model_path}"

class SummonReportInfo:
    def __init__(self):
        self.__summon_path = ""
    
    @property
    def summon_path(self):
        return  self.__summon_path

    @summon_path.setter
    def summon_path(self, path: str):
         self.__summon_path = path

    def __str__(self):
        if  self.__summon_path == "":
            return "当前没有设置生成报告的文件夹"
        return f"当前生成报告的文件夹: {self.__summon_path}"    

class AnalysisReportInfo:
    def __init__(self):
        self.__summon_path = ""
    
    @property
    def analysis_path(self):
        return self.__summon_path

    @analysis_path.setter
    def analysis_path(self, path: str):
         self.__summon_path = path

    def __str__(self):
        if  self.__summon_path == "":
            return "当前没有设置生成分析报告的文件夹"
        return f"当前生成分析报告的文件夹: {self.__summon_path}"  

class InfoPackage:
    def __init__(self):
        self.__image_package = None
        self.__model_package = None
        self.__summon_package = None
        self.__analysis_package = None

    @property
    def image_info(self):
        return self.__image_package
    
    @image_info.setter
    def image_info(self, imageInfo: ImageInfo):
        self.__image_package = imageInfo

    @property
    def model_info(self):
        return self.__model_package
    
    @model_info.setter
    def model_info(self, model_info: ModelInfo):
        self.__model_package = model_info

    @property
    def summon_package(self):
        return self.__summon_package
    
    @summon_package.setter
    def summon_package(self, summon_package: SummonReportInfo):
        self.__summon_package = summon_package

    @property
    def analysis_package(self):
        return self.__analysis_package
    
    @analysis_package.setter
    def analysis_package(self, analysis_package: SummonReportInfo):
        self.__analysis_package = analysis_package
