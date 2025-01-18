from Core.Common.image_utils import ImageUtils
import os
from pathlib import Path

class PathUtils:
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

    """
        check the exsitance
    """
    @staticmethod
    def check_if_exsits_all(paths: list[str]) -> list[bool]:
        reqs = []
        for each_one in paths:
            reqs.append(os.path.exists(each_one))
        return reqs

