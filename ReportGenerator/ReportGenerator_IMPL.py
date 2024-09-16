from Utils.Utils import Software_Utils


class ReportGenerator_Impl:
    def __init__(self):
        self.src_path = ""
        self.gen_path = ""


    def set_generate_path(self, gen_path: str):
        self.gen_path = gen_path

    def set_src_path(self, src_path: str):
        self.src_path = src_path

    def generate_doc(self):
        # Current IMPL
        Software_Utils.copy_file(src=self.src_path, dst=self.gen_path)
