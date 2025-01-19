from PySide6.QtCore import QObject, Signal
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
import torch
from Core.WaveSpliter import ImageWavePraser
from Core.Common.path_utils import PathUtils
from loguru import logger
from cv2 import Mat
from Core.ModelHandler.WrappedDataSet import WrappedImageSet
import numpy as np


class ModelHandler(QObject):
    """ 
        this private signals are used in index the percentage of 
        the model training 
    """
    postFinishedPercentage = Signal(float)


    """
        transform we using
    """

    def __init__(self, parent : QObject = None):
        super().__init__(parent)
        self.__holding_model = ""
        self.__imagewave_parser = ImageWavePraser()
        self.cached_result: list[bool] = []
        
    @property
    def holding_model(self):
        return self.__holding_model
    
    @holding_model.setter
    def holding_model(self, path: str):
        self.__holding_model = path

    def set_save_middlewares(self, req_save, middle_save = PathUtils.SPLIT_PATH):
        self.__imagewave_parser.req_save_in_dir = req_save
        if req_save:
            self.__imagewave_parser.write_path = middle_save
        

    def do_execute_check(self, image_path: str) -> bool:
        return self.__do_execute_for_one(image_path)


    """
        the real one handled
    """
    def __do_execute_for_one(self, image_path: str):
        self.__imagewave_parser.file_name = PathUtils.gain_names_from_paths([image_path])
        images_wait_handle = self.__imagewave_parser.analysis_image(image_path)  
        logger.info(f"Gain the splition size {len(images_wait_handle)}")
        return self.__do_execute_for_one_impl(images_wait_handle)

    """
        handling core
    """
    def __do_execute_for_one_impl(self, image_lists: list[Mat]) -> bool:
        activate_model = torch.load(self.__holding_model, weights_only=False)
        activate_dataset = WrappedImageSet(image_lists, None, transforms.Compose([
            transforms.ToPILImage(),
            transforms.ToTensor()
        ]))
        batch_size = 1
        dataLoader = DataLoader(activate_dataset, batch_size)
        prediction : list[bool] = []
        with torch.no_grad():
            for times, data in enumerate(dataLoader):
                test_prediction = activate_model(data.cuda())
                test_label = np.argmax(test_prediction.cpu().data.numpy(), axis=1)
                for y in test_label:
                    prediction.append(bool(y))    
        result = 2 * sum(prediction) >= len(prediction)   
        self.cached_result.append(result)
        return result
    