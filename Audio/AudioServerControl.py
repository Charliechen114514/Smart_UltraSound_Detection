import pyaudio
import json
import threading
from PyQt6.QtCore import QObject, pyqtSignal
from vosk import Model, KaldiRecognizer

class AudioServer(QObject):
    signal_tell_recognize = pyqtSignal(str)
    audio_interface = None

    def __init__(self, parent=None, channels=1, rate=44100, frames_per_buffer=1024):
        super().__init__(parent)
        self.channels = channels
        self.rate = rate
        self.frames_per_buffer = frames_per_buffer
        self.stream = None
        self.frames = []
        self.model = Model("Audio/vosk-model-small-cn-0.22")

        self.is_recording = False

    def start_recording(self):
        print("开始录音")
        AudioServer.audio_interface = pyaudio.PyAudio()
        self.stream = AudioServer.audio_interface.open(format=pyaudio.paInt16,
                                                       channels=self.channels,
                                                       rate=self.rate,
                                                       input=True,
                                                       frames_per_buffer=self.frames_per_buffer)
        self.is_recording = True
        self.frames = []

        threading.Thread(target=self.record).start()

    def record(self):
        while self.is_recording:
            data = self.stream.read(self.frames_per_buffer)
            self.frames.append(data)

    def stop_recording(self):
        print("结束录音")
        self.is_recording = False
        self.stream.stop_stream()
        self.stream.close()
        if AudioServer.audio_interface is not None:
            AudioServer.audio_interface.terminate()
        self.__do__recognize_callback()

    def __do__recognize_callback(self):
        rec = KaldiRecognizer(self.model, self.rate)
        rec.SetWords(True)
        str_ret = ""
        for data in self.frames:
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                if 'text' in result:
                    str_ret += result['text']

        result = json.loads(rec.FinalResult())
        if 'text' in result:
            str_ret += result['text']

        str_ret = "".join(str_ret.split())
        self.signal_tell_recognize.emit(str_ret)
