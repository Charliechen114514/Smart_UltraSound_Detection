import cv2
import numpy as np
import torch
from torch.utils.data import Dataset
default_size = (256, 256)


class WrappedImageSet(Dataset):
    def __init__(self, x, y=None, transform=None):
        self.x = x
        # label is required to be a LongTensor
        self.y = y
        if y is not None:
            self.y = torch.LongTensor(y)
        self.transform = transform

    def __len__(self):
        return len(self.x)

    def __getitem__(self, index):
        X = self.x[index]
        if self.transform is not None:
            X = self.transform(X)
        if self.y is not None:
            Y = self.y[index]
            return X, Y
        else:  # 如果没有标签那么只返回X
            return X


class ImageProcessor:
    def __init__(self, paths_of_images: list[str]):
        self.image_lists = paths_of_images
        self.resizeSize = default_size
        self.final_images: list[np.array] = []

    def __read_images(self):
        faults = []
        for each_image_path in self.image_lists:
            each_image = cv2.imread(each_image_path)
            if each_image is None:
                faults.append(each_image_path)
            # Resize also
            each_image = cv2.resize(each_image, default_size)
            # Append
            self.final_images.append(each_image)
        return faults

    def make_process(self):
        # Load Images first
        faults = self.__read_images()
        if len(faults) != 0:
            return faults, []
        else:
            return faults, self.final_images

