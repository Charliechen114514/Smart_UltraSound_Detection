import os

import pytesseract
from OCR.ImageOCR_Preprocessors import OCRImage_Preprocessor
from Utils.Utils import Software_Utils


class OCRTextCore:
    @staticmethod
    def get_text_from_image_for_params(image_path: str):
        os.environ.__setitem__("TESSDATA_PREFIX", "./OCR/tessdata/")
        result = {'text': "", 'success': False}
        if not Software_Utils.is_file_exist(image_path):
            return result
        ocr_pre_handler = OCRImage_Preprocessor(image_path)
        ocr_pre_handler.make_threshold(140)
        image = ocr_pre_handler.get_image_format()
        try:
            result = {'text': str(pytesseract.image_to_string(image, "eng")),
                      'success': True}
        except Exception as e:
            raise e

        return result

    @staticmethod
    def get_text_from_image_for_suggestions(image_path: str):
        os.environ.__setitem__("TESSDATA_PREFIX", "./OCR/tessdata/")
        result = {'text': "", 'success': False}
        if not Software_Utils.is_file_exist(image_path):
            return result
        ocr_pre_handler = OCRImage_Preprocessor(image_path)
        image = ocr_pre_handler.get_image_format()
        try:
            result = {'text': str(pytesseract.image_to_string(image, "chi_sim")),
                      'success': True}
        except Exception as e:
            raise e
        return result
