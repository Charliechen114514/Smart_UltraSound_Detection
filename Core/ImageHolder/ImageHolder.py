from loguru import logger
from Core.Common import PathUtils

class ImageHolder:
    INVALID_INDEX: int = -1
    def __init__(self):
        logger.debug("setup the image holder")
        self.__imageList: list[str] = []
        self.__current_index = ImageHolder.INVALID_INDEX
        pass

    def push_images_from_dirent(self, folder_path: str):
        self.__push_images_fromList(PathUtils.gain_all_images(folder_path))

    def push_images_from_paths(self, images: list[str], req_check: bool = False):
        self.__push_images_fromList(images)

    def __push_images_fromList(self, imageList: list[str]):
        self.__imageList = list(set(self.__imageList) | set(imageList))
        logger.trace(f"images are {self.__imageList}")
        self.__current_index = len(self.__imageList) - 1
        
    def image_list_size(self) -> int:
        return len(self.__imageList)

    def image_list(self) -> list[str]:
        return self.__imageList
    
    def remove_by_paths(self, target: list[str]):
        logger.trace(f"will remove the {target} in image holder!")
        self.__imageList = list(set(self.__imageList) - set(target))

    def remove_by_name(self, target: list[str]):
        _paths = PathUtils.get_path_from_base_name(names=target, paths=self.__imageList)
        logger.trace(f"will remove the {_paths} in image holder!")
        self.__imageList = list(set(self.__imageList) - set(_paths))
        
    def gain_paths_from_names(self, target: list[str]) -> list[str]:
        return PathUtils.get_path_from_base_name(names=target, paths=self.__imageList)

    def gain_names_all(self, req_sorted=False):
        if req_sorted:
            return sorted(PathUtils.gain_names_from_paths(self.__imageList))
        return PathUtils.gain_names_from_paths(self.__imageList)
    
    def switch_next_image(self) -> str:
        if len(self.__imageList) == 0:
            return ""
        self.__current_index += 1
        if self.__current_index >= len(self.__imageList):
            self.__current_index = 0
        return self.current_indexed_path()
    
    def switch_prev_image(self) -> str:
        if len(self.__imageList) == 0:
            return ""
        self.__current_index -= 1
        if self.__current_index <= -1:
            self.__current_index = len(self.__imageList) - 1
        return self.current_indexed_path()

    def switch_for_indexed_image(self, index: int) -> str:
        if index < 0 or index >= len(self.__imageList):
            raise "Invalid index given!"
        self.__current_index = index
        return self.current_indexed_path()

    def current_indexed_path(self) -> str:
        if len(self.__imageList) == 0:
            raise "Error for the Empty set imageList operations"
        return self.__imageList[self.__current_index]

    def clear(self):
        self.__imageList.clear()

    def __check_image_list_for_debug(self):
        logger.trace("check the image lists: ")
        for each_image in self.__imageList:
            logger.trace(each_image)
