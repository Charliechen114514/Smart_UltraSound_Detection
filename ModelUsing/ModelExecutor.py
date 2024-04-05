from PyQt6.QtCore import QFile, QObject, pyqtSignal
from torch.utils.data import DataLoader
from ModelUsing.ImageProcessor import *
import torchvision.transforms as transforms
import torch

test_transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.ToTensor()
])


class ModelExecutor(QObject):
    finish_x = pyqtSignal(int)
    finish_all = pyqtSignal()

    def __init__(self, path: str, parent: QObject = None):
        super().__init__(parent)
        self.image_processor = None
        self.path_of_model = path

    def make_inform_faults(self, faults: list[str]):
        res = str()
        for each_fault in faults:
            res += "无法锁定图片位置: " + each_fault + "\n"
        return res

    def __recognize(self):
        current_model = torch.load(self.path_of_model)
        faults, post_images = self.image_processor.make_process()
        if len(faults) != 0:
            return faults, []
        tmp_data_set = WrappedImageSet(post_images, None, test_transform)
        # Set the batch size as 1
        img_loader = DataLoader(tmp_data_set, 1)
        prediction = []

        with torch.no_grad():
            for i, data in enumerate(img_loader):
                test_prediction = current_model(data.cuda())
                test_label = np.argmax(test_prediction.cpu().data.numpy(), axis=1)
                for y in test_label:
                    prediction.append(y)
                    self.finish_x.emit(i)
                    print("Handing prediction " + str(i) + "pic")
        self.finish_all.emit()
        return faults, prediction

    def is_model_accessible(self):
        return QFile.exists(self.path_of_model)

    def load_images_path_and_make_init(self, paths: list[str]):
        self.image_processor = ImageProcessor(paths)

    def make_predictions(self):
        if self.image_processor is None:
            return [], []

        faults, res = self.__recognize()
        if len(faults) != 0:
            return faults, []
        return faults, res
