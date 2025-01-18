import cv2
import os
import numpy as np
from loguru import logger
from Core.Common.path_utils import PathUtils

"""
    Author: zhucan0712
    Github: https://github.com/zhucan0712
    Descriptions: 
        This is the image wave spliter provided by zhucan0712, and the code
        tidy up, optimizations by me
"""

class ImageWavePraser:
    M_PI = 3.14159265358979323846
    default_size = (256, 256)
    def __init__(self):
        self.__write_path = ""
        self.__file_name = ""
        self.__possible_saving_paths: list[str] = []
        self.__images_summon: list[cv2.Mat] = []

        # this controls whether we need
        self.req_save_in_dir = False

    @property
    def write_path(self):
        return self.__write_path
    
    @write_path.setter
    def write_path(self, path: str):
        logger.trace("set the write dirent for a waiting check: " + path)
        self.__write_path = path

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, path: str):
        self.__file_name = path

    def get_possible_saving_paths(self):
        return self.__possible_saving_paths

    def clear_res(self):
        self.__images_summon.clear()
        self.__possible_saving_paths.clear()

    """
        this is the main functions provided!
    """
    def analysis_image(self, path: str) -> list[cv2.Mat]:
        self.__precheck()
        image_cloned = cv2.imread(path)
        if image_cloned is None:
            raise "Image given is blank!"
        process = image_cloned.copy()
        process = self.__preWork(process)
        self.__findMyContours(process, image_cloned)
        logger.info("finish the current check, ready to throw back result")
        return self.__images_summon


    def __precheck(self):
        logger.info("starting check...")
        if not self.req_save_in_dir:
            logger.info("split issue at this time don't required save to the disk...")
            return
        logger.info("wave detection requires the savings, turn into check the path if is required")
        if self.__write_path == "":
            logger.error("The saving path is not specified! with great possible of breaking down!")
        elif not PathUtils.check_paths_if_exsit(self.__write_path):
            logger.warning("The target file_path is not exsit, trying to create one...")
            PathUtils.create_dirent_if_not_exsited(self.__write_path)
        else:
            logger.info("pass the check of the savings...")
        
        if self.file_name == "":
            logger.warning("file name not specified... the image file name will be blank!")

        logger.info("With the check is done!")

    @staticmethod
    def __preWork(src):
        src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        src = cv2.GaussianBlur(src, (3, 3), 0)
        _, src = cv2.threshold(src, 100, 255, cv2.THRESH_BINARY)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        src = cv2.dilate(src, kernel)
        src = cv2.erode(src, kernel)
        src = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)
        return src

    @staticmethod
    def __AMPD(data):
        p_data = [0] * len(data)
        count = len(data)
        arr_rowsum = []

        for k in range(1, count // 2 + 1):
            row_sum = 0
            for i in range(k, count - k):
                if data[i] > data[i - k] and data[i] > data[i + k]:
                    row_sum -= 1
            arr_rowsum.append(row_sum)

        min_index = np.argmin(arr_rowsum)
        max_window_length = min_index

        for k in range(1, max_window_length + 1):
            for i in range(k, count - k):
                if data[i] > data[i - k] and data[i] > data[i + k]:
                    p_data[i] += 1

        peak_indices = [i for i in range(count) if p_data[i] == max_window_length]
        if len(peak_indices) == 0:
            return [0]
        return peak_indices

    @staticmethod
    def __autocorr(signal):
        N = len(signal)
        autocorr_values = [0.0] * N

        for lag in range(N):
            for n in range(N - lag):
                autocorr_values[lag] += signal[n] * signal[n + lag]

        return autocorr_values

    def __getCycle(self, srcImage):
        resMat = srcImage.copy()
        srcImage = self.__preWork(srcImage)
        erange = 0.3
        width = srcImage.shape[1]
        height = srcImage.shape[0]
        projectValArry = [0] * width

        for col in range(width):
            for row in range(height):
                if srcImage[row, col] == 0:
                    projectValArry[col] += 1

        verticalProjectionMat_1 = np.full((height, width), 255, dtype=np.uint8)
        for i in range(width):
            verticalProjectionMat_1[height - projectValArry[i]:height, i] = 0

        vec = projectValArry
        peaks = self.__AMPD(vec)
        autocorr_values = self.__autocorr(vec)
        cycles = self.__AMPD(autocorr_values)
        cycle = cycles[0]
        if cycle < 100 and len(cycles) > 1:
            cycle = cycles[1]

        repeaks = []
        for i in range(len(peaks)):
            x = peaks[i] if i == 0 else peaks[i] - peaks[i - 1]
            n = int(x / cycle)
            q = x / cycle - n
            if q > erange:
                n += 1
            if n >= 1:
                for j in range(n):
                    repeaks.append(peaks[i] - (j - 1) * cycle)
            else:
                repeaks.append(peaks[i])

        t = len(repeaks) - 1
        x = width - repeaks[t]
        n = int(x / cycle)
        q = x / cycle - n
        if q < erange:
            n -= 1
        if n >= 1:
            for j in range(n):
                repeaks.append(repeaks[t] + cycle * (n - j + 1))

        if len(repeaks) > 1:
            firstPeak = repeaks[0]
            if firstPeak < cycle:
                repeaks.pop(0)

            lastPeak = repeaks[-1]
            remainingWidth = width - lastPeak
            if remainingWidth < cycle:
                repeaks.pop()

            i = 1
            while i < len(repeaks) - 1:
                currentPeak = repeaks[i]
                nextPeak = repeaks[i + 1]
                distance = nextPeak - currentPeak
                if distance < cycle:
                    mergePoint = (currentPeak + nextPeak) / 2.0
                    repeaks[i] = mergePoint
                    repeaks.pop(i + 1)
                else:
                    i += 1

        resultImages = []
        if len(repeaks) < 10 and cycle > 50:
            for i in range(len(repeaks)):
                peakIndex = int(repeaks[i])
                if i == 0:
                    region = resMat[:, :peakIndex]
                elif i == len(repeaks) - 1:
                    region = resMat[:, peakIndex:]
                else:
                    nextPeakIndex = int(repeaks[i + 1])
                    region = resMat[:, peakIndex:nextPeakIndex]
                if region.shape[0] > 0 and region.shape[1] > 0:
                    resultImages.append(region)

            for i, img in enumerate(resultImages):
                summon_name = os.path.join(f"{self.__write_path}", f"{self.__file_name}-{i + 1}.png")
                img = cv2.resize(img, ImageWavePraser.default_size)
                self.__images_summon.append(img)
                if self.req_save_in_dir:
                    self.__possible_saving_paths.append()
                    logger.trace(f"summon one wave which will be possibly written to:{summon_name}")
                    cv2.imwrite(f"{self.__write_path}{self.__file_name}-{i + 1}.png", img)

    def __findMaxHeight(self, src, target):
        calculate = [pt for pt in target if 1 < pt[0][0] < src.shape[1] - 5 and 1 < pt[0][1] < src.shape[0] - 10]

        rect = cv2.boundingRect(np.array(calculate))
        roi = src[rect[1]:rect[1] + rect[3], rect[0]:rect[0] + rect[2]]
        if roi.shape[0] > 0 and roi.shape[1] > 0:
            self.__getCycle(roi)

    def __findMyContours(self, src, org):
        contours, _ = cv2.findContours(src, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        target = [sig for sig in contours if cv2.contourArea(sig) > 1000]

        AfterEffect = org.copy()
        mask = np.zeros(src.shape, dtype=np.uint8)
        cv2.drawContours(mask, target, -1, 255, thickness=cv2.FILLED)
        src[mask == 0] = 255
        self.__findMaxHeight(AfterEffect, target[0])


