import re
from Core.OCR.ImageOCR import OCRTextCore


class ReportAnalysisCore:
    def __init__(self, text: str):
        self.handle_text_list = list(filter(None, text.split("\n")))
        print(self.handle_text_list)

    def __handle_PI(self, strings: str) -> str:
        if len(strings) <= 3:
            return strings
        else:
            cur_number = float(strings[1:-1])
            if cur_number <= 1:
                return str(cur_number)
            while cur_number >= 100:
                cur_number /= 100
            return str(cur_number)


    def __handle_HR(self, strings: list[str]) -> str:
        if len(strings) <= 3:
            return "0"
        return strings[len(strings) - 3]

    def analysis_numbers(self):
        res_dict = {
            "PS": 0,
            "RI": 0,
            "ED": 0,
            "MD": 0,
            "S/D": 0,
            "TAMax": 0,
            "PI": 0,
            "HR": 0
        }
        # start from the line 7 though
        index_bounder_below = 6
        index_bounder_upper = 9
        if len(self.handle_text_list) <= 10:
            return res_dict

        # Get PS RI here
        current_text = self.handle_text_list[index_bounder_below]
        pattern = r"(?<!\d)-?\d+\.\d+(?!\d)"
        matches = re.findall(pattern, current_text)
        print(matches)
        res_dict['PS'] = matches[0]
        res_dict['RI'] = matches[1]

        current_text = self.handle_text_list[index_bounder_below + 1]
        pattern = r"(?<!\d)(?:<\s*-?\d+|-?\d+)\.\d*0\b|(?<!\d)(?:<\s*-?\d+|-?\d+)\.\d*[1-9](?!\d)"
        matches = re.findall(pattern, current_text)
        print(matches)
        res_dict['ED'] = matches[0]
        matches[1] = matches[1].replace("<", "-").replace(">", "-")
        res_dict['MD'] = matches[1]

        current_text = self.handle_text_list[index_bounder_upper - 1]
        pattern = r"(?<!\d)-?\d+\.\d+(?!\d)"
        matches = re.findall(pattern, current_text)
        print(matches)
        # Fetch the first and the last
        res_dict['S/D'] = str(round(float(matches[0]), 2))
        res_dict['TAMax'] = str(round(float(matches[len(matches) - 1]), 2))

        current_text = self.handle_text_list[index_bounder_upper]
        pattern = r"-?\d+\.\d+|-?\d+"
        matches = re.findall(pattern, current_text)
        print(matches)
        res_dict['PI'] = self.__handle_PI(matches[0])
        res_dict['HR'] = self.__handle_HR(matches)

        print(res_dict)
        return res_dict

    @staticmethod
    def gain_advice(text: str) -> str:
        texts_raw = list(filter(None, text.split("\n")))
        print(texts_raw)
        text = ""
        flag = False
        for each in texts_raw:
            if each.find("意见") != -1:
                flag = True
                continue
            if flag:
                text += each
        return text
