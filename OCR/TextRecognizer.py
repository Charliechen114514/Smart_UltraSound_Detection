from OCR.TextRecognizerCore import TextRecoginzerCore


class TextRecognizer:
    def __init__(self):
        self.getting_core = TextRecoginzerCore()
        self.all_text = ""

    def get_all_text(self, image_path: str, req_re_recognize: bool = True):
        if self.all_text is "" or req_re_recognize:
            try:
                self.all_text = self.getting_core.get_all_text(image_path)
            except Exception as e:
                raise e
        return self.all_text

    def handle_text(self, image_path: str):
        self.get_all_text(image_path)
        self.__check_text()

    def __check_text(self):
        pass
