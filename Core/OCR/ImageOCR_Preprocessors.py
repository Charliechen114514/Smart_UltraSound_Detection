import cv2
from PIL import Image


class OCRImage_Preprocessor:
    def __init__(self, image_path):
        self.__image_path = image_path
        self.__preprocessing_image = None

    def __load_if_none(self):
        if self.__preprocessing_image is None:
            self.__preprocessing_image = cv2.imread(self.__image_path)
            self.__preprocessing_image = cv2.cvtColor(self.__preprocessing_image, cv2.COLOR_BGR2GRAY)

    def make_blur(self, blur_core_size: int):
        self.__load_if_none()
        cv2.medianBlur(self.__preprocessing_image, blur_core_size)
        # cv2.imshow("demo", self.__preprocessing_image)
        # cv2.waitKey(0)

    def make_threshold(self, threshold: int):
        self.__load_if_none()
        self.__preprocessing_image = cv2.threshold(self.__preprocessing_image, threshold, 255,
                                                   cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        # cv2.imshow("demo", self.__preprocessing_image)
        # cv2.waitKey(0)

    def get_image_format(self):
        if self.__preprocessing_image is None:
            self.__preprocessing_image = cv2.imread(self.__image_path)
            self.__preprocessing_image = cv2.cvtColor(self.__preprocessing_image, cv2.COLOR_BGR2GRAY)
        return Image.fromarray(cv2.cvtColor(self.__preprocessing_image, cv2.COLOR_BGR2RGB))
