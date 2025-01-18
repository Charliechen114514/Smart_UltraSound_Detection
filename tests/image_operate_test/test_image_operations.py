import os, sys
from loguru import logger
from Core.ImageHolder import ImageHolder
from Core.Common import PathUtils

# level switching
logger.add(sys.stdout, level="DEBUG")
"""
    This is a test that promise the image operations.
"""

class SimpleImageImporter:
    test_image_path_dirent = "tests/image_operate_test/images"
    def __init__(self):
        logger.trace("set up the original comparision class ...")
        self.__image_list = []
        pass

    def __pvt_load_images(self):
        self.__image_list += PathUtils.gain_all_images(self.test_image_path_dirent)

    def image_lists(self) -> list[str]:
        return self.__image_list
    
    def image_sizes(self) -> int:
        return len(self.__image_list)

    def setup(self):
        self.__pvt_load_images()

"""
    test image insertions
"""
def test_insert_image():
    logger.trace("loading the test of the insertions")
    image_Holder = ImageHolder()
    image_Holder.push_images_from_dirent(SimpleImageImporter.test_image_path_dirent)

    compare_case = SimpleImageImporter()
    compare_case.setup()

    logger.trace("about test the image size issue")
    assert compare_case.image_sizes() == image_Holder.image_list_size()

def test_insert_image_name_same():
    logger.trace("loading the test of the insertions names")
    image_Holder = ImageHolder()
    image_Holder.push_images_from_dirent(SimpleImageImporter.test_image_path_dirent)

    compare_case = SimpleImageImporter()
    compare_case.setup()

    assert set(image_Holder.image_list()) == set(compare_case.image_lists())

def test_duplicate_insertion():
    """ import as the set """
    logger.trace("loading the test of the insertions")
    image_Holder = ImageHolder()
    image_Holder.push_images_from_dirent(SimpleImageImporter.test_image_path_dirent)
    image_Holder.push_images_from_dirent(SimpleImageImporter.test_image_path_dirent)

    compare_case = SimpleImageImporter()
    compare_case.setup()
    logger.trace("about test the image duplicate insertion issue...")
    assert compare_case.image_sizes() == image_Holder.image_list_size()

def test_remove_list():
    logger.trace("loading the test of the remove")
    image_Holder = ImageHolder()
    image_Holder.push_images_from_dirent(SimpleImageImporter.test_image_path_dirent)
    original_size = image_Holder.image_list_size()
    target = ['deleted1', 'deleted2']
    image_Holder.remove_by_name(target)

    compare_case = SimpleImageImporter()
    compare_case.setup()

    logger.trace("asserting if removing is successful")
    assert original_size - 2 == image_Holder.image_list_size()
    logger.trace("asserting if removing's is correct")
    checking_paths = PathUtils.get_path_from_base_name(['deleted1', 'deleted2'], compare_case.image_lists())
    
    logger.trace("asserting if PathLibs work is correct")
    paths = image_Holder.image_list()
    assert len(checking_paths) == 2
    for each_check in checking_paths:
        assert paths.count(each_check) == 0

    """
        test the remove of none-exsits
    """
    size = image_Holder.image_list_size()
    image_Holder.remove_by_name(['delete3'])
    assert image_Holder.image_list_size() == size



