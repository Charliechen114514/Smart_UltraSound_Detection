from Core.Common.path_utils import PathUtils
import shutil
from loguru import logger
from configparser import ConfigParser
from Core.config.config_keys import *
import tools.download as dwload

# 运行前配置
accept_non_ssl: bool = False
download_audio_url = "https://alphacephei.com/vosk/models/vosk-model-small-cn-0.22.zip"

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

# 检查是否存在vosk语音包
logger.info("Checking the runtime full dependencies")
if not PathUtils.check_paths_if_exsit("Core/Audio/vosk-model-small-cn-0.22"):
    logger.error("Audio Package is not exsited, fetching from remote...")
    logger.info("pre-Building for the tmp")
    PathUtils.create_dirent_if_not_exsited(PathUtils.TMP_PATH)
    logger.info("pre-Building for the tmp done")
    logger.info("Start issuing the download...")

    logger.info("Download the Audio Server required")
    result = dwload.download_and_extract(
        download_audio_url, 
        PathUtils.TMP_PATH,
        "Core/Audio/"
    )
    if result:
        logger.info("Issue down")
    else:
        logger.error("As the audio server is unable to access, Audio Server is disabled...")
else:
    logger.info("Audio Server is expected!")
    