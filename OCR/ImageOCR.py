import pytesseract
from PIL import (Image)
from Utils.Utils import Software_Utils


class OCRTextCore:
    @staticmethod
    def get_text_from_image(image_path: str):
        result = {'text': "", 'success': False}
        if not Software_Utils.is_file_exist(image_path):
            return result

        image = Image.open(image_path)
        try:
            result = {'text': str(pytesseract.image_to_string(image, "eng")), 'success': True}
        except Exception as e:
            raise e

        return result
