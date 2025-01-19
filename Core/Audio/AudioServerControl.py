import pyaudio
import json
import threading
from PySide6.QtCore import QObject, Signal
from vosk import Model, KaldiRecognizer
import logging
import time
from loguru import logger
import numpy as np

# Disabled the other loggings
logging.basicConfig(level=logging.CRITICAL)
class AudioServer(QObject):
    signal_tell_recognize = Signal(str)
    signal_tell_shutdown = Signal()
    audio_interface = None
    critical_time = 1.5
    silence_threshold = 20

    def __init__(self, parent=None, channels=1, rate=44100, frames_per_buffer=1024):
        super().__init__(parent)
        self.channels = channels
        self.__rate = rate
        self.__frames_per_buffer = frames_per_buffer
        self.__stream = None
        self.__frames = []
        self.__model = Model("Core/Audio/vosk-model-small-cn-0.22")
        self.__rec = KaldiRecognizer(self.__model, self.__rate)
        self.__rec.SetWords(True)
        self.is_recording = False

    def start_recording(self):
        logger.info("开始录音")
        AudioServer.audio_interface = pyaudio.PyAudio()
        self.__stream = AudioServer.audio_interface.open(format=pyaudio.paInt16,
                                                       channels=self.channels,
                                                       rate=self.__rate,
                                                       input=True,
                                                       frames_per_buffer=self.__frames_per_buffer)
        self.is_recording = True
        self.__frames = []
        threading.Thread(target=self.__record).start()

    def stop_recording(self):
        logger.info("结束录音")
        self.is_recording = False
        self.__stream.stop_stream()
        self.__stream.close()
        if AudioServer.audio_interface is not None:
            AudioServer.audio_interface.terminate()
        self.__do__recognize_callback()

    def __record(self):
        last_audio_time = time.time()
        while self.is_recording:
            data = self.__stream.read(self.__frames_per_buffer)
            self.__frames.append(data)
            
            audio_data = np.frombuffer(data, dtype=np.int16)
            volume = np.nan_to_num(np.sqrt(np.abs(np.mean(np.square(audio_data)))))
            
            # 判断是否为静默
            if volume < AudioServer.silence_threshold:
                if time.time() - last_audio_time > AudioServer.critical_time:
                    logger.info("with no sound detected, auto handling")
                    self.signal_tell_shutdown.emit()
                    self.stop_recording()
                    break
            else:
                last_audio_time = time.time()


    def __do__recognize_callback(self):
        str_ret = ""
        for data in self.__frames:
            if self.__rec.AcceptWaveform(data):
                result = json.loads(self.__rec.Result())
                if 'text' in result:
                    str_ret += result['text']

        result = json.loads(self.__rec.FinalResult())
        if 'text' in result:
            str_ret += result['text']

        str_ret = "".join(str_ret.split())
        self.signal_tell_recognize.emit(str_ret)
