from ReportAnalysis.DocxSourcesGetter import DocxSourcesGetter
from ReportAnalysis.ReportAnalysisCore import ReportAnalysisCore
from WordDocxGenerator.DocxGenerator import DocxGenerator


class DocxGenerator_IMPL:
    def __init__(self, passing_text: str):
        self.__advice = None
        self.__core = ReportAnalysisCore(passing_text)
        self.__docx_gen = DocxGenerator()
        self.__period = True

    def set_period(self, period: bool):
        self.__period = period

    def set_path(self, path: str):
        self.__docx_gen.set_path(path)

    def __create_each_index_title(self, title_name: str, value: float, shell_mark_red: int, append_after_value: str):
        para = self.__docx_gen.add_paragraph(title_name)
        if shell_mark_red:
            self.__docx_gen.append_paragraph(para, str(value) + append_after_value, [255, 0, 0])
        else:
            # Normal
            self.__docx_gen.append_paragraph(para, str(value) + append_after_value, [0, 0, 0])

    def __create_each_index_title_for_int_val(self, title_name: str, value: int, shell_mark_red: int,
                                              append_after_value: str):
        para = self.__docx_gen.add_paragraph(title_name)
        if shell_mark_red:
            self.__docx_gen.append_paragraph(para, str(value) + append_after_value, [255, 0, 0])
        else:
            # Normal
            self.__docx_gen.append_paragraph(para, str(value) + append_after_value, [0, 0, 0])

    def __create_each_index_sources(self, text: str):
        self.__docx_gen.add_paragraph(text)

    def __set_heading(self, text: str, level: int, req_center: bool):
        self.__docx_gen.add_heading(text, level, req_center)

    def create_docx_sources(self):
        self.__set_heading("报告解析结果", 1, True)
        self.__set_heading("一．血流动力学指标分析", 2, False)
        gen_doct = self.__core.analysis_numbers()

        # PS
        sources = DocxSourcesGetter.gain_block_PS()
        self.__create_each_index_title("1.收缩期流速PS：", float(gen_doct['PS']), False, "cm/s")
        self.__create_each_index_sources(sources)

        # ED
        sources = DocxSourcesGetter.gain_block_ED()
        self.__create_each_index_title("2.舒张期流速ED：", float(gen_doct['ED']), False, "cm/s")
        self.__create_each_index_sources(sources)

        # SD
        sources, value = DocxSourcesGetter.gain_block_SD(float(gen_doct['S/D']), self.__period)
        self.__create_each_index_title("3.收缩期/舒张期比值S/D：", float(gen_doct['S/D']), value != 0,
                                       DocxSourcesGetter.gain_label_accord_value(value))
        self.__create_each_index_sources(sources)

        # PI
        sources, value = DocxSourcesGetter.gain_block_PI(float(gen_doct['PI']), self.__period)
        self.__create_each_index_title("4.脉冲指数PI：", float(gen_doct['PI']), value != 0,
                                       DocxSourcesGetter.gain_label_accord_value(value))
        self.__create_each_index_sources(sources)

        # RI
        sources, value = DocxSourcesGetter.gain_block_RI(float(gen_doct['RI']), self.__period)
        self.__create_each_index_title("阻力指数RI：", float(gen_doct['RI']), value != 0,
                                       DocxSourcesGetter.gain_label_accord_value(value))
        self.__create_each_index_sources(sources)

        # MD
        sources, value = DocxSourcesGetter.gain_block_MD(float(gen_doct['MD']))
        self.__create_each_index_title("平均血流速度MD：", float(gen_doct['MD']), value != 0,
                                       "cm/s" + DocxSourcesGetter.gain_label_accord_value(value))
        self.__create_each_index_sources(sources)

        # TAMax
        sources, value = DocxSourcesGetter.gain_block_TAmax(float(gen_doct['TAMax']), self.__period)
        self.__create_each_index_title("最高血流速度TAmax：", float(gen_doct['TAMax']), value != 0,
                                       "cm/s" + DocxSourcesGetter.gain_label_accord_value(value))
        self.__create_each_index_sources(sources)

        # HR
        sources, value = DocxSourcesGetter.gain_block_HR(float(gen_doct['HR']))
        self.__create_each_index_title_for_int_val("心率HR：", int(gen_doct['HR']), value != 0,
                                                   DocxSourcesGetter.gain_label_accord_value(value))
        self.__create_each_index_sources(sources)

        # Advices
        if self.__advice is None:
            return

        self.__set_heading("二．智能诊断意见", 2, False)
        self.__create_each_index_sources("    " + self.__advice)

    def set_advice(self, text: str):
        self.__advice = ReportAnalysisCore.gain_advice(text)

    def save_docx(self):
        try:
            self.__docx_gen.save_this()
        except Exception as e:
            raise e
