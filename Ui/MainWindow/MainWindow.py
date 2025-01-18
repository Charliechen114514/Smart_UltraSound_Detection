# Loggings...
import sys
from loguru import logger
# Pyside Dependencies
from PySide6 import QtWidgets
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtGui import QPixmap
# Private Dependences
from Ui.Common import UiUtils
from Core.ImageHolder import ImageHolder
from Core.ModelHandler import ModelHandler
from . import Ui_MainWindow
from Ui.BrowsingGuide.BrowsingGuide import BrowsingGuide

"""
    MainWindow is the Main Interactive Window work as the top level 
    interactive adapter with user and the applications
"""
class MainWindow(QtWidgets.QMainWindow):
    def __setup_logger(self):
        logger.add(sys.stdout, level="TRACE")

    """
        This is the initializations of the mainWindow
    """
    def __init__(self, parent = None):
        self.__setup_logger()
        logger.trace("entering initialize...")
        super().__init__(parent)
        # Memory init
        self.__image_holder = ImageHolder()
        self.__browsing_guide = BrowsingGuide()
        self.__model_handler = ModelHandler()
        # Setup Ui Form from Ui_MainWindow
        self.__Ui = Ui_MainWindow()
        self.__Ui.setupUi(self)
        self.__post_init_ui()
        # connections setup
        self.__init_connections()

    """
        using in loading images by selecting dirent
    """
    def on_loadImagesBySelectingFolders(self):
        paths = UiUtils.fetch_selected_dirent(self, "选择导入的文件夹")
        if paths == "":
            logger.debug("User don't select any folder, quit the process")
            return
        logger.debug(f"User select folder: {paths}")
        self.__image_holder.push_images_from_dirent(paths)

        # Load the image
        path = self.__image_holder.current_indexed_path()
        self.__load_image_work(path)
        self.__on_change_the_ui_when_images_flash()

    """
        using in loading images by selecting files
    """
    def on_loadImagesBySelectingPaths(self):
        paths = UiUtils.fetch_selected_files(self, "选择（可复选）文件")
        if len(paths) == 0:
            logger.debug("User don't select any images, quit the process")
            return
        logger.debug(f"User select folder: {paths}")
        self.__image_holder.push_images_from_paths(paths)

        # Load the image
        path = self.__image_holder.current_indexed_path()
        self.__load_image_work(path)
        self.__on_change_the_ui_when_images_flash()

    """
        moving the next images
    """
    def on_switch_next_image(self):
        path = self.__image_holder.switch_next_image()
        logger.trace(f"will handle the path: {path}")
        self.__load_image_work(path)
        self.__on_change_the_ui_when_images_flash()

    """
        moving the previous images
    """
    def on_switch_prev_image(self):
        path = self.__image_holder.switch_prev_image()
        logger.trace(f"will handle the path: {path}")
        self.__load_image_work(path)
        self.__on_change_the_ui_when_images_flash()

    """
        moving the given indexed images
    """
    def on_switch_given_index_image(self, index: int):
        logger.trace(f"receiving the index: {index}")
        path = self.__image_holder.switch_for_indexed_image(index)
        logger.trace(f"will handle the path: {path}")
        self.__load_image_work(path)
        self.__on_change_the_ui_when_images_flash()

    """
        handling the model import
    """
    def on_handle_model_import(self):
        model_path = UiUtils.fetch_selected_file(self, "选择目标检索模型")
        if model_path == "":
            logger.debug("User don't select any model, quit the process")
            return
        self.__model_handler.holding_model = model_path
        logger.trace(f"User selected the model: {self.__model_handler.holding_model}")


    """
        def private_load given image_path
    """
    def __load_image_work(self, path: str):
        pixmap: QPixmap = QPixmap(path).scaled(self.__Ui.label_display.size())
        self.__Ui.label_display.setPixmap(pixmap)
    
    """
        fresh the ui when images are changed
    """
    def __on_change_the_ui_when_images_flash(self):
        left_size = self.__image_holder.image_list_size()
        self.__Ui.action_next_image.setEnabled(left_size != 0)
        self.__Ui.action_prev_image.setEnabled(left_size != 0)
        if left_size == 0:
            self.__browsing_guide.reset_as_clean()
        else:
            self.__browsing_guide.set_totol_size(left_size)
 
        names_display = self.__image_holder.gain_names_all()
        self.__Ui.listWidget_selections.addItems(names_display)

    """
        done after user quit
    """
    def finalize(self):
        # do the finalize when the exec is quited
        logger.trace("entering finalize...")
        logger.remove()

# ------------------- Private ------------------------
    def __post_init_ui(self):
        self.__Ui.toolBar.insertWidget(self.__Ui.action_prev_image, self.__browsing_guide)

    def __init_connections(self):
        """toolbar and menubar actions connnections"""
        self.__Ui.action_import_folder.triggered.connect(self.on_loadImagesBySelectingFolders)
        self.__Ui.action_import_images.triggered.connect(self.on_loadImagesBySelectingPaths)
        self.__Ui.action_next_image.triggered.connect(self.on_switch_next_image)
        self.__Ui.action_prev_image.triggered.connect(self.on_switch_prev_image)     
        self.__Ui.action_import_models.triggered.connect(self.on_handle_model_import)

        """
            list widget ui
        """
        self.__Ui.listWidget_selections.itemClicked.connect(self.__on_item_clicked)
        
        """
            other part of ui
        """
        self.__browsing_guide.postIndex.connect(self.on_switch_given_index_image)

    """
        handling the item clicked
    """
    def __on_item_clicked(self, item: QListWidgetItem):
        logger.trace(f"item clicked! item text: {item.text()}")
        path = self.__image_holder.gain_paths_from_names([item.text()])
        logger.trace(f"will handle the path: {path[0]}")
        self.__load_image_work(path[0])





