from Core.Common.path_utils import PathUtils
import shutil
from loguru import logger
from configparser import ConfigParser
from Core.config.config_keys import *

# 运行时配置
config_file_path: str = 'Core/config/config.ini'
sections = [SECTION_PATH]
required_keys = [MODEL_PATH, ANALYSIS_PATH, REPORT_PATH]

def copy_blank_config_file():
    source_file = 'Core/config/config.ini.tmpl'
    destination_file = config_file_path
    shutil.copy(source_file, destination_file)

def check_ini_file(file_path: str):
    config = ConfigParser()
    try:
        logger.trace("trying to load the file")
        config.read(file_path)
        
        if not config.sections():
            logger.warning("Error for is possible missing file!")
            return False
        
        for section in sections:
            if section not in config.sections():
                logger.warning(f"section '{section}' is missing")
                return False
        
        # 检查是否包含所有的关键字
        for key in required_keys:
            if key not in config[section]:
                logger.warning(f"keyword '{key}' is missing in '{section}'")
                return False
            
        logger.info("Pass the check of the file")
        return True
    except Exception as e:
        logger.warning(f"Error when loading: {e}")
        return False

# 设置目标路径
logger.info("pre-Building for the RC Transformations")
PathUtils.create_dirent_if_not_exsited(PathUtils.RC_PATH)
logger.info("pre-Building for the RC Transformations done")

logger.info("pre-Building for ini file check")
# 检查ini文件是否正常
if not check_ini_file(config_file_path):
    logger.warning("original ini file corrupted! reset to the initial state...")
    copy_blank_config_file()
logger.info("pre-Building for ini file check done!")