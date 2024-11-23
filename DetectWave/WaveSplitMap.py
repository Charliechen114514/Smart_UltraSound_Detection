import os
import collections
from Utils.Utils import Software_Utils
class WaveSplitMap:
    def __init__(self):
        self.map = collections.OrderedDict()

    def entryFile(self, path: str):
        self.map[Software_Utils.get_file_name_accord_path(path)] = path

    def gain_path_by_file_name_match(self, file_name: str):
        _file_name = file_name.split('.')[0]
        return self.map[_file_name]

    def gain_size(self) -> int:
        return len(self.map.keys())
