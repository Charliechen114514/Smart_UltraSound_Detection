# Loggings...
import sys
from loguru import logger
# Pyside Dependencies
from PySide6 import QtWidgets
from PySide6.QtCore import QPoint, Qt
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QMenu, QMessageBox
from PySide6.QtGui import QPixmap, QAction, QCursor
# Private Core and Utils Dependences
from Ui.Common import UiUtils
from Core.ImageHolder import ImageHolder
from Core.ModelHandler import ModelHandler
from Core.AnalysisReport import AnalysisReportHandler
from Core.SummonReport import SummonReportHandler
from Core.config.config_operate import MainWindowConfigure 
from Core.config.config_keys import *
from Core.Common.path_utils import PathUtils
# Ui Dependencies
from . import Ui_MainWindow
from Ui.BrowsingGuide.BrowsingGuide import BrowsingGuide
from Ui.InfoWindow.InfoWindow import InfoWindow
from Core.InfoPackage.InfoPackage   import InfoPackage, ImageInfo, \
                                    ModelInfo, SummonReportInfo, AnalysisReportInfo


"""
    MainWindow is the Main Interactive Window work as the top level 
    interactive adapter with user and the applications
"""
class MainWindow(QMainWindow):
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
        self.__model_handler = ModelHandler(self)
        self.__summonReportHandle = SummonReportHandler()
        self.__analysisReportHandle = AnalysisReportHandler()

        self.__custemMenu = QMenu(self)
        self.__infoWindow = None
        # Setup Ui Form from Ui_MainWindow
        self.__Ui = Ui_MainWindow()
        self.__Ui.setupUi(self)
        self.__post_init_ui()
        # connections setup
        self.__init_connections()
        # configure setup
        self.__on_load_config_from_file()


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
        if path == "":
            logger.info("image set turns none!")
            self.__on_change_the_ui_when_images_flash()
            return
        logger.trace(f"will handle the path: {path}")
        self.__load_image_work(path)
        self.__on_change_the_ui_when_images_flash()

    """
        moving the previous images
    """
    def on_switch_prev_image(self):
        path = self.__image_holder.switch_prev_image()
        if path == "":
            logger.info("image set turns none!")
            self.__on_change_the_ui_when_images_flash()
            return
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
        self.__load_model_impl(model_path)

    """
        handle the message check
    """
    def on_handle_check(self):
        if self.__infoWindow is None:
            self.__infoWindow = InfoWindow()
        self.__on_setup_checkinfo_window()
        self.__infoWindow.show()

    """
        handle the delete_request on current_item
    """
    def on_handle_current_delete(self):
        selected_item = self.__Ui.listWidget_selections.currentItem()
        if not selected_item:
            logger.debug("no item is seleted!")
            return
        logger.debug(f"about remove the item {selected_item.text()}")
        self.__image_holder.remove_by_name([selected_item.text()])
        self.on_switch_next_image()

    """
        handle the summon path set
    """
    def on_handle_summon_path_set(self):
        path = UiUtils.fetch_selected_dirent(self, "选择文件夹")
        self.__Ui.label_report_path.setText(f"报告解析小程序位置: {path}")
        self.__set_summon_report_path_impl(path)


    """
        handle the analysis path set
    """
    def on_handle_analysis_path_set(self):
        path = UiUtils.fetch_selected_dirent(self, "选择文件夹")
        self.__Ui.label_analysis_report.setText(f"报告生成路径位于: {path}")
        self.__set_analysis_report_path_impl(path)
        
    """
        on start recognize the current item issue
    """
    def on_recognize_current_item_issue(self):
        item = self.__Ui.listWidget_selections.currentItem()
        if not item:
            QMessageBox.critical(self, "发生错误", "请在左侧列表选择需要检测的报告单进行检测")
            return
        current_path = self.__image_holder.gain_paths_from_names([item.text()])[0]
        result = self.__model_handler.do_execute_check([current_path])
        logger.info(f"Current item check result is: {result}!")

    """
        handling the analysis
    """
    def on_handle_analysis(self):
        path = UiUtils.fetch_selected_file(self, "选择报告文件", ".",\
                                filters=UiUtils.makeup_image_filters())
        if path == "":
            logger.debug("User select nothing! quit process")
            return
        self.__analysisReportHandle.handling_image_report = path
        try:
            self.__analysisReportHandle.analysis_report()
        except Exception as e:
           logger.error(str(e))
           QMessageBox.critical(self, "发生错误！",
                                 "发生错误: " + str(e) + ", \n很有可能您正在打开待写入文件！请关闭后重试！")


    """
        done after user quit
    """
    def finalize(self):
        # log back
        self.__on_load_back_ini()
        # do the finalize when the exec is quited
        logger.trace("entering finalize...")
        logger.remove()

# ------------------- Private ------------------------

    """
        on load the ini file
    """
    def __on_load_config_from_file(self):
        configure = MainWindowConfigure()
        configure.read_from_file()
        dict_exp = configure.expose_dict()
        # Load Paths
        self.__load_model_impl(dict_exp[MODEL_PATH])
        self.__set_summon_report_path_impl(dict_exp[REPORT_PATH])
        self.__set_analysis_report_path_impl(dict_exp[ANALYSIS_PATH])

    """
        on load back ini
    """
    def __on_load_back_ini(self):
        configure = MainWindowConfigure()
        dict_of_cache = configure.expose_dict()
        dict_of_cache[MODEL_PATH] = self.__model_handler.holding_model
        dict_of_cache[ANALYSIS_PATH] = self.__analysisReportHandle.analysis_folder
        dict_of_cache[REPORT_PATH] = self.__summonReportHandle.summon_folder 
        try:
            configure.write_back_file()
        except Exception as e:
            QMessageBox.critical(self, "写配置文件发生错误!", "发生写配置文件错误!" + str(e))

    """
        impls for the model initialize
    """
    def __load_model_impl(self, model_path: str):
        if model_path == "":
            logger.debug("User don't select any model, quit the process")
            return
        if not PathUtils.check_paths_if_exsit(model_path):
            logger.warning(f"model path {model_path} owns value but seemingly not exsits...")
            return
        self.__model_handler.holding_model = model_path
        self.__on_possible_enabled_the_summon_group()
        logger.trace(f"User selected the model: {self.__model_handler.holding_model}")

    """
        impls for the summon report path set
    """
    def __set_summon_report_path_impl(self, path: str):
        if path == "":
            logger.trace("user selected empty dir, quit the process")
            self.__on_possible_enabled_the_summon_group()
            return
        if not PathUtils.check_paths_if_exsit(path):
            logger.warning(f"summon_path {path} owns value but seemingly not exsits...")
            self.__on_possible_enabled_the_summon_group()
            return
        logger.trace(f"user selected dir {path}")
        self.__summonReportHandle.summon_folder = path
        self.__on_possible_enabled_the_summon_group()

    """
        impls for the analysis report path set
    """
    def __set_analysis_report_path_impl(self, path: str):   
        if path == "":
            logger.trace("user selected empty dir, quit the process")
            self.__on_enabled_the_analysis_group(False)
            return
        if not PathUtils.check_paths_if_exsit(path):
            logger.warning(f"analysis_path: {path}owns value but seemingly not exsits...")
            self.__on_enabled_the_analysis_group(False)
            return        
        
        logger.trace(f"user selected dir {path}")
        self.__analysisReportHandle.analysis_folder = path
        self.__on_enabled_the_analysis_group(True)

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
        self.__on_possible_enabled_the_summon_group()
        self.__Ui.action_next_image.setEnabled(left_size != 0)
        self.__Ui.action_prev_image.setEnabled(left_size != 0)
        if left_size == 0:
            self.__browsing_guide.reset_as_clean()
        else:
            self.__browsing_guide.set_total_size(left_size)
 
        names_display = self.__image_holder.gain_names_all()
        self.__Ui.listWidget_selections.clear()
        self.__Ui.listWidget_selections.addItems(names_display)


    def __post_init_ui(self):
        self.__Ui.toolBar.insertWidget(self.__Ui.action_prev_image, self.__browsing_guide)
        delete_action = QAction("删除选中项", self)
        self.__custemMenu.addAction(delete_action)
        delete_action.triggered.connect(self.on_handle_current_delete)
        self.__Ui.listWidget_selections.setContextMenuPolicy(Qt.CustomContextMenu)
    
    def __init_connections(self):
        """toolbar and menubar actions connnections"""
        self.__Ui.action_import_folder.triggered.connect(self.on_loadImagesBySelectingFolders)
        self.__Ui.action_import_images.triggered.connect(self.on_loadImagesBySelectingPaths)
        self.__Ui.action_next_image.triggered.connect(self.on_switch_next_image)
        self.__Ui.action_prev_image.triggered.connect(self.on_switch_prev_image)     
        self.__Ui.action_import_models.triggered.connect(self.on_handle_model_import)
        self.__Ui.action_check_infos.triggered.connect(self.on_handle_check)
        
        """
            list widget ui
        """
        self.__Ui.listWidget_selections.itemClicked.connect(self.__on_item_clicked)
        self.__Ui.listWidget_selections.customContextMenuRequested.connect(self.__onshowCustomizeMenu)
        
        """
            other part of ui
        """
        self.__browsing_guide.postIndex.connect(self.on_switch_given_index_image)
        self.__Ui.btn_set_analysis_path.pressed.connect(self.on_handle_analysis_path_set)
        self.__Ui.btn_set_summon_path.pressed.connect(self.on_handle_summon_path_set)
        self.__Ui.btn_summon_report_for_current.pressed.connect(self.on_recognize_current_item_issue)
        self.__Ui.btn_analysis_report.pressed.connect(self.on_handle_analysis)
    
    """
        handling the item clicked
    """
    def __on_item_clicked(self, item: QListWidgetItem):
        logger.trace(f"item clicked! item text: {item.text()}")
        path = self.__image_holder.gain_paths_from_names([item.text()])
        logger.trace(f"will handle the path: {path[0]}")
        self.__load_image_work(path[0])

    def __onshowCustomizeMenu(self, point: QPoint):
        logger.trace("on entering the customize!")
        if self.__image_holder.image_list_size() == 0:
            logger.debug("No images are in the list, denied the show!")
            return
        logger.trace(f"the menu will be shown at {point}")
        self.__custemMenu.exec_(QCursor.pos())

    def __on_enabled_the_analysis_group(self, enabled: bool = True):
        self.__Ui.action_analysis_report.setEnabled(enabled)
        self.__Ui.btn_analysis_report.setEnabled(enabled)

    def __on_possible_enabled_the_summon_group(self):
        enabled :bool = \
            self.__image_holder.image_list_size() != 0 and \
                self.__model_handler.holding_model != "" and \
                self.__summonReportHandle.summon_folder != ""
        self.__Ui.btn_summon_report_for_all.setEnabled(enabled)
        self.__Ui.btn_summon_report_for_current.setEnabled(enabled)
        self.__Ui.action_summon_report_for_all.setEnabled(enabled)
        self.__Ui.action_summon_report_for_current.setEnabled(enabled)

    """
        handling the package setup
    """
    def __on_setup_checkinfo_window(self):
        # set up the packages required
        package = InfoPackage()

        imageInfo = ImageInfo()
        imageInfo.image_size = self.__image_holder.image_list_size()
        package.image_info  = imageInfo

        model_info = ModelInfo()
        model_info.model_path = self.__model_handler.holding_model
        package.model_info = model_info

        summon_info = SummonReportInfo()
        summon_info.summon_path = self.__summonReportHandle.summon_folder
        package.summon_package = summon_info

        analysis_info = AnalysisReportInfo()
        analysis_info.analysis_path = self.__analysisReportHandle.analysis_folder
        package.analysis_package = analysis_info

        self.__infoWindow.setInfo(package)
