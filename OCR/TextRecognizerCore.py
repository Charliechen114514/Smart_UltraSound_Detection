import os

from OCR.ImageOCR import OCRTextCore
from Utils.Utils import Software_Utils


class TextRecoginzerCore:
    TESS_DATA = "OCR/tessdata"
    TESS_DATA_ENV_NAME = 'TESSDATA_PREFIX'

    def __init__(self):
        self.tess_data_path = Software_Utils.from_rela_path_to_abs_path(TextRecoginzerCore.TESS_DATA)
        self.load_tess_date()
        self.current_text = ""

    def load_tess_date(self):
        os.environ[TextRecoginzerCore.TESS_DATA_ENV_NAME] = self.tess_data_path

    def get_all_text(self, image_path: str) -> str:
        try:
            self.current_text = OCRTextCore.get_text_from_image(image_path)
        except Exception as e:
            raise e
        return self.current_text
