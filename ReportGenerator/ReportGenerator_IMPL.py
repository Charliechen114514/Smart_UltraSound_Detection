from Utils.Utils import Software_Utils


class ReportGenerator_Impl:
    def __init__(self):
        self.__gen_dir = ""

    def set_generate_dir(self, dir: str):
        self.__gen_dir = dir

    def get_generate_dir(self) -> str:
        return self.__gen_dir

    def generate_doc(self):
        pass
