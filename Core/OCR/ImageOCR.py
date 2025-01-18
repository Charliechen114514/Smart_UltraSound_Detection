import os
import pytesseract
from Core.OCR.ImageOCR_Preprocessors import OCRImage_Preprocessor
from Core.Common.path_utils import PathUtils


class OCRTextCore:
    @staticmethod
    def get_text_from_image_for_params(image_path: str):
        os.environ["TESSDATA_PREFIX"] = "Core/OCR/tessdata"
        result = {'text': "", 'success': False}
        if not PathUtils.check_paths_if_exsit(image_path):
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
        os.environ["TESSDATA_PREFIX"] = "Core/OCR/tessdata"
        result = {'text': "", 'success': False}
        if not PathUtils.check_paths_if_exsit(image_path):
            return result
        ocr_pre_handler = OCRImage_Preprocessor(image_path)
        image = ocr_pre_handler.get_image_format()
        try:
            result = {'text': str(pytesseract.image_to_string(image, "chi_sim")),
                      'success': True}
        except Exception as e:
            raise e
        return result
