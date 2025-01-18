import cv2
import numpy as np
import pytesseract

"""
    Author: zhucan0712
    Github: https://github.com/zhucan0712
    Descriptions: 
    This is the driver helps provide infos of 8 params, 
    which code that help fetch necessary params helping generate reports
    
    Created by zhucan0712, majoring in Computer Version Core Work
    Validate and modified bugs by Charliechen 
"""

class FetchParamDriver:
    def __init__(self):
        self.__res = []
        pass

    def __findMyCountours(self, src, org):
        contours, _ = cv2.findContours(src, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        target = []
        for sig in contours:
            area = cv2.contourArea(sig)
            if area > 1000:
                target.append(sig)

        AfterEffect = org.copy()
        calculate = self.__findMaxHeight(AfterEffect, target[0])
        return calculate

    def __preWork(self, src):
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

        src = cv2.GaussianBlur(src, (3, 3), 0)

        _, src = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        src = cv2.dilate(src, kernel)

        src = cv2.erode(src, kernel)

        src = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)

        return src

    def __recognizeText(self, roi):
        custom_config = r'--psm 6 -c tessedit_char_whitelist=0123456789'
        ocr = pytesseract.image_to_string(roi, lang='anums', config=custom_config)
        return ocr

    def __findverticalUnit(self, src, org):
        contours, _ = cv2.findContours(src, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        verticalValues = []

        for contour in contours:
            boundingBox = cv2.boundingRect(contour)
            if boundingBox[2] > boundingBox[3] and boundingBox[3] < 5:
                center = (boundingBox[0] + boundingBox[2] // 2, boundingBox[1] + boundingBox[3] // 2)
                numberBox = (max(center[0] - 40, 0), max(center[1] - 15, 0),
                             min(80, src.shape[1] - max(center[0] - 40, 0)),
                             min(30, src.shape[0] - max(center[1] - 15, 0)))

                numberRoi = org[numberBox[1]:numberBox[1] + numberBox[3], numberBox[0]:numberBox[0] + numberBox[2]]
                numberText = self.__recognizeText(numberRoi)

                if numberText:
                    try:
                        numValue = int(numberText)
                        # print("识别的数值: ", numValue, ", 坐标: ", center)
                        verticalValues.append((center[1], numValue))
                    except ValueError:
                        pass

        verticalUnit = 0.2
        if len(verticalValues) > 1:
            pixelToValueRatios = []
            for i in range(1, len(verticalValues)):
                pixelDiff = verticalValues[i][0] - verticalValues[i - 1][0]
                valueDiff = verticalValues[i][1] - verticalValues[i - 1][1]
                if pixelDiff != 0:
                    ratio = abs(float(valueDiff) / pixelDiff)
                    if 0.1 <= ratio <= 0.8:
                        pixelToValueRatios.append(ratio)

            if pixelToValueRatios:
                verticalUnit = sum(pixelToValueRatios) / len(pixelToValueRatios)

        return verticalUnit

    # 计算垂直投影直方图
    def __calculateVerticalProjection(self, srcImage):
        resMat = srcImage.copy()
        process = srcImage.copy()
        process = self.__preWork(process)

        width = srcImage.shape[1]
        height = srcImage.shape[0]
        projectValArry = np.zeros(width, dtype=int)

        for col in range(width):
            for row in range(height):
                perPixelValue = process[row, col]
                if perPixelValue == 0:
                    projectValArry[col] += 1

        vec = projectValArry.tolist()

        return vec

    # 计算指标的函数
    def __calculateMetrics(self, roi, repeaks, revalleys, cycle, verticalUnit):
        width = roi.shape[1]
        height = roi.shape[0]

        process = roi.copy()
        process = self.__preWork(process)

        calculate = self.__findMyCountours(process, roi)
        calculates = [calculate]

        axisY = 0
        for contour in calculates:
            for point in contour:
                if axisY == 0 or point[0][1] > axisY:
                    axisY = point[0][1]

        axisY = height - axisY

        PS = 0
        ED = 0
        MD = 0
        TAmax = 0
        if cycle < 50 or cycle > 300:
            cycle = 130
        HR = cycle

        peakValues = []
        valleyValues = []

        for peak in revalleys:
            if 0 <= peak < width:
                peakValue = height
                for contour in calculates:
                    for point in contour:
                        if point[0][0] == int(peak):
                            peakValue = min(peakValue, point[0][1])

                peakValues.append((height - peakValue - axisY) * verticalUnit)

        for valley in repeaks:
            if 0 <= valley < width:
                valleyValue = height
                for contour in calculates:
                    for point in contour:
                        if point[0][0] == int(valley):
                            valleyValue = min(valleyValue, point[0][1])

                valleyValues.append((height - valleyValue - axisY) * verticalUnit)

        if peakValues:
            PS = max(peakValues)
        if valleyValues:
            ED = min(valleyValues)

        if valleyValues:
            sum_val = sum(valleyValues)
            MD = sum_val / len(valleyValues)

        if len(repeaks) >= 4:
            start = int(repeaks[1])
            end = int(repeaks[3])

            sumHeights = 0
            count = 0

            for contour in calculates:
                for point in contour:
                    if start <= point[0][0] <= end:
                        sumHeights += height - point[0][1]
                        count += 1

            if count > 0:
                TAmax = (sumHeights / count) * verticalUnit

        S_D = PS / ED if ED != 0 else 0
        PI = (PS - ED) / TAmax if TAmax != 0 else 0
        RI = (PS - ED) / PS if PS != 0 else 0

        self.__res.append(round(PS, 2))
        self.__res.append(round(ED, 2))
        self.__res.append(round(S_D, 2))
        self.__res.append(round(PI, 2))
        self.__res.append(round(RI, 2))
        self.__res.append(round(MD, 2))
        self.__res.append(round(TAmax, 2))
        self.__res.append(round(HR, 2))

    # 将 int 向量转换为 double 向量
    @staticmethod
    def convertToDoubleVector(intVec):
        return [float(x) for x in intVec]

    # 检测波峰或波谷
    # 参数 type 决定检测波峰还是波谷
    # 0: 检测波峰
    # 1: 检测波谷
    def __AMPD(self, data, type):
        p_data = [0] * len(data)
        count = len(data)
        arr_rowsum = []

        for k in range(1, count // 2 + 1):
            row_sum = 0
            for i in range(k, count - k):
                if type == 0:
                    if data[i] > data[i - k] and data[i] > data[i + k]:
                        row_sum -= 1
                elif type == 1:
                    if data[i] < data[i - k] and data[i] < data[i + k]:
                        row_sum -= 1

            arr_rowsum.append(row_sum)

        min_index = np.argmin(arr_rowsum)
        max_window_length = min_index

        for k in range(1, max_window_length + 1):
            for i in range(k, count - k):
                if type == 0:
                    if data[i] > data[i - k] and data[i] > data[i + k]:
                        p_data[i] += 1
                elif type == 1:
                    if data[i] < data[i - k] and data[i] < data[i + k]:
                        p_data[i] += 1

        peak_indices = [i for i, x in enumerate(p_data) if x == max_window_length]
        if not peak_indices:
            peak_indices = [0]

        return peak_indices

    # 计算信号的自相关函数
    # 峰值即为周期
    def __autocorr(self, signal):
        N = len(signal)
        autocorr_values = np.zeros(N)

        for lag in range(N):
            for n in range(N - lag):
                autocorr_values[lag] += signal[n] * signal[n + lag]

        return autocorr_values.tolist()

    # 得到优化后的波峰波谷值
    def __Revalues(self, values, width, cycle):
        erange = 0.3
        revalues = []

        for i in range(len(values)):
            x = 0
            if i == 0:
                x = values[0]
            else:
                x = values[i] - values[i - 1]

            n = int(x / cycle)
            q = x / cycle - n
            if q > erange:
                n += 1

            if n >= 1:
                for j in range(n, 0, -1):
                    revalues.append(values[i] - (j - 1) * cycle)
            else:
                revalues.append(values[i])

        t = len(revalues) - 1
        x = width - revalues[t]
        n = int(x / cycle)
        q = x / cycle - n
        if q < erange:
            n -= 1

        if n >= 1:
            for j in range(n, 0, -1):
                revalues.append(revalues[t] + cycle * (n - j + 1))

        if len(revalues) > 1:
            if revalues[0] < cycle:
                revalues.pop(0)

            lastPeak = revalues[-1]
            remainingWidth = width - lastPeak
            if remainingWidth < cycle:
                revalues.pop()

            for i in range(1, len(revalues) - 2):
                if i >= len(revalues) - 1:
                    break
                currentPeak = revalues[i]
                nextPeak = revalues[i + 1]
                distance = nextPeak - currentPeak
                if distance < cycle:
                    mergePoint = (currentPeak + nextPeak) / 2.0
                    revalues[i] = mergePoint
                    revalues.pop(i + 1)
                    i -= 1
                else:
                    break

        return revalues

    # 得到图像像素垂直直方图
    # 据波谷位置和周期分割图像
    def __getCycle(self, srcImage, vertialUnit):
        resMat = srcImage.copy()
        process = srcImage.copy()
        process = self.__preWork(process)

        width = srcImage.shape[1]
        height = srcImage.shape[0]
        projectValArry = np.zeros(width, dtype=int)

        for col in range(width):
            for row in range(height):
                perPixelValue = process[row, col]
                if perPixelValue == 0:
                    projectValArry[col] += 1

        vec = projectValArry.tolist()

        peaks = self.__AMPD(vec, 0)
        valleys = self.__AMPD(vec, 1)

        autocorr_values = self.__autocorr(vec)
        cycles = self.__AMPD(autocorr_values, 0)
        cycle = cycles[0]
        if cycle < 100 and len(cycles) > 1:
            cycle = cycles[1]

        revalleys = self.__Revalues(valleys, width, cycle)
        repeaks = self.__Revalues(peaks, width, cycle)

        self.__calculateMetrics(resMat, repeaks, revalleys, cycle, vertialUnit)

    def __findMaxHeight(self, src, target):
        calculate = [pt for pt in target if 1 < pt[0][0] < src.shape[1] - 5 and 1 < pt[0][1] < src.shape[0] - 10]
        return calculate

    def fetch_params(self, path: str) -> list[float]:
        a = cv2.imread(path)
        if a is None:
            return []
        bimg = a.copy()
        c = a.copy()
        process = a.copy()
        resMat = a.copy()
        bimg = bimg[int(bimg.shape[0] * 0.6):int(bimg.shape[0] * 0.9), :]

        proimg = bimg.copy()
        proimg = self.__preWork(proimg)
        verticalUnit = self.__findverticalUnit(proimg, bimg)

        process = self.__preWork(process)
        calculate = self.__findMyCountours(process, c)
        rect = cv2.boundingRect(np.array(calculate))
        roi = resMat[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
        self.__getCycle(roi, verticalUnit)
        return self.__res

    def clear_previous(self):
        self.__res.clear()

    def echo_value(self):
        if len(self.__res) != 8:
            print("Error in fetch value, you may not have fetch the value:)")
            return
        print("PS: ", self.__res[0])
        print("ED: ", self.__res[1])
        print("S/D: ", self.__res[2])
        print("PI: ", self.__res[3])
        print("RI: ", self.__res[4])
        print("MD: ", self.__res[5])
        print("TAmax: ", self.__res[6])
        print("HR: ", self.__res[7])
