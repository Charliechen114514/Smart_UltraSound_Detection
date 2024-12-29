from ReportAnalysis.DocxSourcesGetter import DocxSourcesGetter

class SuggestionsFetcher:
    SD_HIGH_SUGGEST = "S/D比值偏高通常提示胎儿缺氧、胎盘功能不全。进行胎心监护和胎盘评估。"
    SD_LOW_SUGGEST = "较低的S/D比值通常表示脐动脉的血流阻力较低，通常不表示问题，但应结合其他指标综合评估胎儿的健康情况"

    PI_HIGH_SUGGEST = ("PI值过高通常表示脐动脉血流的脉动幅度增大，可能由于胎盘血流受限、胎儿缺氧或胎盘功能不良引起。可能需要进一步的评估和监测，"
                       "以确定胎儿健康状况，并考虑是否需要干预措施，如更频繁的监测或考虑提前分娩。")
    PI_LOW_SUGGEST = "PI值偏低通常不表示问题,但应结合其他指标综合评估胎儿的健康情况。"

    RI_HIGH_SUGGEST = "RI偏高通常提示胎盘血流不畅，可能影响胎儿健康，应结合其他指标，考虑进一步监测或住院观察。"
    RI_LOW_SUGGEST = "较低的RI值通常不表示问题,但应结合其他指标综合评估胎儿的健康情况。"

    MD_HIGH_SUGGEST = "MD值偏高通常提示胎儿缺氧、胎盘功能不全。应详细评估胎儿状况，可能需要讨论分娩计划。"
    MD_LOW_SUGGEST = "低MD值通常提示胎盘供血不足或胎儿存在缺氧风险。需要进一步评估胎盘功能和胎儿状况，可能需要采取额外的监测和干预措施。"

    TAmax_HIGH_SUGGEST = "TAmax值偏高提示胎儿可能处于应激状态。应密切监测胎儿状况，必要时考虑进行详细的胎心监护。"
    TAmax_LOW_SUGGEST = "低TAmax值通常提示胎盘供血不足或胎儿缺氧，需要结合其他血流动力学指标和临床症状进行进一步评估，以确定是否需要干预或监测。"

    HR_HIGH_SUGGEST = "HR偏高通常提示胎儿窘迫或应激反应。应进行胎心监护，考虑进一步检查。"
    HR_LOW_SUGGEST = ("胎儿心率偏低可能提示胎儿缺氧、胎盘血流不足、脐带压迫或其他问题。需要迅速评估，以确定是否需要紧急处理或干预，医生可能会建议"
                      "采取措施来改善胎儿的氧供，如母体体位调整、给予氧气或进行其他治疗。")

    @staticmethod
    def __gain_block_SD(value: float, _period: bool) -> str:
        suggest = ""

        if _period:
            value = DocxSourcesGetter.check_index_in_range(value, 3, 4.5)
        else:
            value = DocxSourcesGetter.check_index_in_range(value, 1.7, 3)

        if value == -1:
            suggest = SuggestionsFetcher.SD_LOW_SUGGEST
        elif value == 1:
            suggest = SuggestionsFetcher.SD_HIGH_SUGGEST
        return suggest

    @staticmethod
    def __gain_block_PI(value: float, _period: bool) -> str:
        suggest = ""

        if _period:
            value = DocxSourcesGetter.check_index_in_range(value, 0.86, 1.2)
        else:
            value = DocxSourcesGetter.check_index_in_range(value, 0.62, 1.24)

        if value == -1:
            suggest = SuggestionsFetcher.PI_LOW_SUGGEST
        elif value == 1:
            suggest = SuggestionsFetcher.PI_HIGH_SUGGEST
        return suggest

    @staticmethod
    def __gain_block_RI(value: float, _period: bool) -> str:
        suggest = ""

        if _period:
            value = DocxSourcesGetter.check_index_in_range(value, 0.6, 0.7)
        else:
            value = DocxSourcesGetter.check_index_in_range(value, 0.45, 0.65)

        if value == -1:
            suggest = SuggestionsFetcher.RI_LOW_SUGGEST
        elif value == 1:
            suggest = SuggestionsFetcher.RI_HIGH_SUGGEST
        return suggest

    @staticmethod
    def __gain_block_MD(value: float) -> str:
        suggest = ""

        value = DocxSourcesGetter.check_index_in_range(abs(value), 30, 60)

        if value == -1:
            suggest = SuggestionsFetcher.MD_LOW_SUGGEST
        elif value == 1:
            suggest = SuggestionsFetcher.MD_HIGH_SUGGEST
        return suggest

    @staticmethod
    def __gain_block_TAmax(value: float, _period: bool) -> str:
        suggest = ""

        if _period:
            value = DocxSourcesGetter.check_index_in_range(abs(value), 20, 60)
        else:
            value = DocxSourcesGetter.check_index_in_range(abs(value), 30, 70)

        if value == -1:
            suggest = SuggestionsFetcher.TAmax_LOW_SUGGEST
        elif value == 1:
            suggest = SuggestionsFetcher.TAmax_HIGH_SUGGEST
        return suggest

    @staticmethod
    def __gain_block_HR(value: float):
        value = DocxSourcesGetter.check_index_in_range(value, 120, 160)
        suggest = ""
        if value == -1:
            suggest = SuggestionsFetcher.HR_LOW_SUGGEST
        elif value == 1:
            suggest = SuggestionsFetcher.HR_HIGH_SUGGEST
        return suggest

    @staticmethod
    def get_advice(infos: list[float], _period=True):
        """
        Index are followings
        print("PS: ", self.__res[0])
        print("ED: ", self.__res[1])
        print("S/D: ", self.__res[2])
        print("PI: ", self.__res[3])
        print("RI: ", self.__res[4])
        print("MD: ", self.__res[5])
        print("TAmax: ", self.__res[6])
        print("HR: ", self.__res[7])
        """
        suggest = "疑似异常情况。"
        suggest += SuggestionsFetcher.__gain_block_SD(infos[2], _period)
        suggest += SuggestionsFetcher.__gain_block_PI(infos[3], _period)
        suggest += SuggestionsFetcher.__gain_block_RI(infos[4], _period)
        suggest += SuggestionsFetcher.__gain_block_MD(infos[5])
        suggest += SuggestionsFetcher.__gain_block_TAmax(infos[6], _period)
        suggest += SuggestionsFetcher.__gain_block_HR(infos[7])

        return suggest



