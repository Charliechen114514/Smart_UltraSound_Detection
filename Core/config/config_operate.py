"""
    This file provides the common read write keys of
    initializer and de-init operations
    this should be used for ini file read write
"""
from configparser import ConfigParser
from Core.config.config_keys import *
from smartultrasound_detection.pre_main import config_file_path
class MainWindowConfigure:
    CONFIG_FILE_PATH = config_file_path
    def __init__(self):
        self.__ini_container = {
            REPORT_PATH: "",
            MODEL_PATH: "",
            ANALYSIS_PATH: ""
        }
        self.__config_parser = ConfigParser()
        self.__config_parser.read(MainWindowConfigure.CONFIG_FILE_PATH)

    def __write_back_to_section(self, section_name: str, key_name: str, value_name: str):
        self.__config_parser.set(section_name, key_name, value_name)

    def __read_from_section(self, section_name: str, key_name: str) -> str:
        return self.__config_parser.get(section_name, key_name)

    def __init_PathSections(self):
        self.__ini_container[REPORT_PATH] = self.__read_from_section(SECTION_PATH, REPORT_PATH)
        self.__ini_container[MODEL_PATH] = self.__read_from_section(SECTION_PATH, MODEL_PATH)
        self.__ini_container[ANALYSIS_PATH] = self.__read_from_section(SECTION_PATH, ANALYSIS_PATH)

    def __de_init_PathSections(self):
        self.__write_back_to_section(SECTION_PATH, REPORT_PATH, self.__ini_container[REPORT_PATH])
        self.__write_back_to_section(SECTION_PATH, MODEL_PATH,self.__ini_container[MODEL_PATH])
        self.__write_back_to_section(SECTION_PATH, ANALYSIS_PATH,self.__ini_container[ANALYSIS_PATH])
        with open(MainWindowConfigure.CONFIG_FILE_PATH, "w") as f:
            self.__config_parser.write(f)

    def expose_dict(self) -> dict:
        return self.__ini_container

    """
        read the config commons
    """
    def read_from_file(self):
        self.__init_PathSections()

    def write_back_file(self):
        self.__de_init_PathSections()
