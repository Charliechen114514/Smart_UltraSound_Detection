TOO_HIGH = "(偏高↑)"
TOO_LOW = "(偏低↓)"
NORMAL = "(正常)"

SD_INTRO = "S/D比值反映了脐动脉血流的阻力情况。"
SD_HIGH_SUGGEST = "S/D比值偏高通常提示胎儿缺氧、胎盘功能不全。进行胎心监护和胎盘评估。"
SD_LOW_SUGGEST = "较低的S/D比值通常表示脐动脉的血流阻力较低，通常不表示问题，但应结合其他指标综合评估胎儿的健康情况"
SD_RANGE = "参考范围：孕早期3-4.5	孕晚期1.7-3"

PI_INTRO = "PI 值用于评估脐动脉的脉动情况和血流阻力。正常的PI值表明脐动脉血流的脉动幅度适中，通常与胎盘功能良好相关。"
PI_HIGH_SUGGEST = ("PI值过高通常表示脐动脉血流的脉动幅度增大，可能由于胎盘血流受限、胎儿缺氧或胎盘功能不良引起。可能需要进一步的评估和监测，"
                   "以确定胎儿健康状况，并考虑是否需要干预措施，如更频繁的监测或考虑提前分娩。")
PI_LOW_SUGGEST = "PI值偏低通常不表示问题,但应结合其他指标综合评估胎儿的健康情况。"
PI_RANGE = "参考范围:孕早期：0.86～1.2	孕晚期：0.62～1.24"

RI_INTRO = "RI 值用于评估脐动脉的血流阻力。正常的RI值表明脐动脉血流正常，血管阻力适中。但若其他指标异常需要综合考虑胎儿的健康情况。"
RI_HIGH_SUGGEST = "RI偏高通常提示胎盘血流不畅，可能影响胎儿健康，应结合其他指标，考虑进一步监测或住院观察。"
RI_LOW_SUGGEST = "较低的RI值通常不表示问题,但应结合其他指标综合评估胎儿的健康情况。"
RI_RANGE = "参考范围:孕早期：0.6~0.7     孕晚期：0.45-0.65"

MD_INTRO = "MD值提供了脐动脉血流的整体情况。"
MD_HIGH_SUGGEST = "MD值偏高通常提示胎儿缺氧、胎盘功能不全。应详细评估胎儿状况，可能需要讨论分娩计划。"
MD_LOW_SUGGEST = "低MD值通常提示胎盘供血不足或胎儿存在缺氧风险。需要进一步评估胎盘功能和胎儿状况，可能需要采取额外的监测和干预措施。"
MD_RANGE = "参考范围：30-60 cm/s"

TAmax_INTRO = "TAmax用于评估脐动脉的整体血流动态，反映了脐动脉的血流情况和胎盘的功能。"
TAmax_HIGH_SUGGEST = "TAmax值偏高提示胎儿可能处于应激状态。应密切监测胎儿状况，必要时考虑进行详细的胎心监护。"
TAmax_LOW_SUGGEST = "低TAmax值通常提示胎盘供血不足或胎儿缺氧，需要结合其他血流动力学指标和临床症状进行进一步评估，以确定是否需要干预或监测。"
TAmax_RANGE = "参考范围：孕早期：20-60 cm/s孕晚期：30-70 cm/s"

HR_INTRO = "胎儿的心率反映了胎儿的心脏健康和功能。"
HR_HIGH_SUGGEST = "HR偏高通常提示胎儿窘迫或应激反应。应进行胎心监护，考虑进一步检查。"
HR_LOW_SUGGEST = ("胎儿心率偏低可能提示胎儿缺氧、胎盘血流不足、脐带压迫或其他问题。需要迅速评估，以确定是否需要紧急处理或干预，医生可能会建议"
                  "采取措施来改善胎儿的氧供，如母体体位调整、给予氧气或进行其他治疗。")
HR_RANGE = "参考范围：120-160 bpm"

PS_BLOCK = ("    PS 反映了脐动脉血流的动力学特征。它可以帮助评估胎盘的血流供应及胎儿是否存在缺氧或其他问题。在实际诊断过程中通常与ED结合，"
            "计算S/D来判断指标是否正常。")
ED_BLOCK = "    ED 反映了胎盘血流在舒张期的情况。在实际诊断过程中通常与PS结合，计算S/D来判断指标是否正常。"


class DocxSourcesGetter:
    @staticmethod
    def check_index_in_range(value: float, lower: float, upper: float):
        if value > upper:
            return 1
        if value < lower:
            return -1
        return 0

    @staticmethod
    def gain_block_PS() -> str:
        return PS_BLOCK

    @staticmethod
    def gain_block_ED() -> str:
        return ED_BLOCK

    @staticmethod
    def gain_block_SD(value: float, _period: bool) -> tuple[str, int]:
        suggest = ""

        if _period:
            value = DocxSourcesGetter.check_index_in_range(value, 3, 4.5)
        else:
            value = DocxSourcesGetter.check_index_in_range(value, 1.7, 3)

        if value == -1:
            suggest = SD_LOW_SUGGEST
        elif value == 1:
            suggest = SD_HIGH_SUGGEST
        block = "    " + SD_INTRO + suggest + "\n    " + SD_RANGE
        return block, value

    @staticmethod
    def gain_block_PI(value: float, _period: bool) -> tuple[str, int]:
        suggest = ""

        if _period:
            value = DocxSourcesGetter.check_index_in_range(value, 0.86, 1.2)
        else:
            value = DocxSourcesGetter.check_index_in_range(value, 0.62, 1.24)

        if value == -1:
            suggest = PI_LOW_SUGGEST
        elif value == 1:
            suggest = PI_HIGH_SUGGEST
        block = "    " + PI_INTRO + suggest + "\n    " + PI_RANGE
        return block, value

    @staticmethod
    def gain_block_RI(value: float, _period: bool) -> tuple[str, int]:
        suggest = ""

        if _period:
            value = DocxSourcesGetter.check_index_in_range(value, 0.6, 0.7)
        else:
            value = DocxSourcesGetter.check_index_in_range(value, 0.45, 0.65)

        if value == -1:
            suggest = RI_LOW_SUGGEST
        elif value == 1:
            suggest = RI_HIGH_SUGGEST
        block = "    " + RI_INTRO + suggest + "\n    " + RI_RANGE
        return block, value

    @staticmethod
    def gain_block_MD(value: float) -> tuple[str, int]:
        suggest = ""

        value = DocxSourcesGetter.check_index_in_range(abs(value), 30, 60)

        if value == -1:
            suggest = MD_LOW_SUGGEST
        elif value == 1:
            suggest = MD_HIGH_SUGGEST
        block = "    " + MD_INTRO + suggest + "\n    " + MD_RANGE
        return block, value

    @staticmethod
    def gain_block_TAmax(value: float, _period: bool) -> tuple[str, int]:
        suggest = ""

        if _period:
            value = DocxSourcesGetter.check_index_in_range(abs(value), 20, 60)
        else:
            value = DocxSourcesGetter.check_index_in_range(abs(value), 30, 70)

        if value == -1:
            suggest = TAmax_LOW_SUGGEST
        elif value == 1:
            suggest = TAmax_HIGH_SUGGEST
        block = "    " + TAmax_INTRO + suggest + "\n    " + TAmax_RANGE
        return block, value

    @staticmethod
    def gain_block_HR(value: float) -> tuple[str, int]:
        value = DocxSourcesGetter.check_index_in_range(value, 120, 160)
        suggest = ""
        if value == -1:
            suggest = HR_LOW_SUGGEST
        elif value == 1:
            suggest = HR_HIGH_SUGGEST
        block = "    " + HR_INTRO + suggest + "\n    " + HR_RANGE
        return block, value

    @staticmethod
    def gain_label_accord_value(value: int):
        if value == -1:
            return TOO_LOW
        elif value == 0:
            return NORMAL
        return TOO_HIGH
