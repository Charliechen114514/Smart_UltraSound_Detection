from Core.Common.image_utils import ImageUtils
import os
from pathlib import Path
from loguru import logger

class PathUtils:
    MIDDLEWARES_ROOT = "runtimes_middlewares"
    RC_PATH = os.path.join(MIDDLEWARES_ROOT, "rc_py")
    TMP_PATH = os.path.join(MIDDLEWARES_ROOT, "tmp")
    SPLIT_PATH = os.path.join(MIDDLEWARES_ROOT, "splits")
    """
        This help gains the images that is support in
        current application
    """
    @staticmethod
    def gain_all_images(dirent: str) -> list[str]:
        image_paths = []
        for root, dir, files in os.walk(dirent):
            for file in files:
                if any(file.lower().endswith(ext) for ext in \
                       ImageUtils.supportive_image_extensions):
                    image_paths.append(os.path.join(root, file))
        return image_paths

    """
        provided the base, we can fetch the paths contains in the paths given
    """
    @staticmethod
    def get_path_from_base_name(names: list[str], paths: list[str]) -> list[str]:
        return [each for each in paths \
                for target_name in names \
                if Path(each).stem == target_name]

    """
        oppsite for the get_path_from_base_name
    """
    @staticmethod
    def gain_names_from_paths(paths: list[str]) -> list[str]:
        return [Path(path).stem for path in paths]

    @staticmethod
    def gain_name_from_path(path: str) -> str:
        return Path(path).stem

    """
        check the exsitance
    """
    @staticmethod
    def check_if_exsits_all(paths: list[str]) -> list[bool]:
        reqs = []
        for each_one in paths:
            reqs.append(os.path.exists(each_one))
        return reqs

    @staticmethod
    def create_dirent_if_not_exsited(dir_path: str):
    # 检查路径是否存在，如果不存在则创建
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            logger.info(f"Directory '{dir_path}' created as is requried")
        else:
            logger.info(f"Directory '{dir_path}' already exists. jump the creations...")

    @staticmethod
    def check_paths_if_exsit(file_or_dir_path: str) -> bool:
        return os.path.exists(file_or_dir_path)