# Loggings...
import sys
from loguru import logger
# Pyside Dependencies
from PySide6 import QtWidgets
from PySide6.QtCore import QPoint, Qt, Signal
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QMenu, QMessageBox, QApplication
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
from Ui.ProcessingWindow.ProcessingWindow import ProcessingWindow
from Ui.SelectiveWindow.SelectiveWindow import SelectiveWindow
from Core.InfoPackage.InfoPackage   import InfoPackage, ImageInfo, \
                                    ModelInfo, SummonReportInfo, AnalysisReportInfo
from Core.Audio.AudioServerControl import AudioServer

"""
    MainWindow is the Main Interactive Window work as the top level 
    interactive adapter with user and the applications
"""
class MainWindow(QMainWindow):

    onReadySummonReport = Signal()
    tellSummonWhere = Signal(str)
    tellResultHow = Signal(str)

    """
        This is the initializations of the mainWindow
    """
    def __init__(self, parent = None):
        self.__setup_logger()
        logger.trace("entering initialize...")
        super().__init__(parent)
        # Memory init
        self.__audioServer = None
        
        self.__image_holder = ImageHolder()
        self.__browsing_guide = BrowsingGuide()
        self.__model_handler = ModelHandler(self)
        self.__summonReportHandle = SummonReportHandler()
        self.__analysisReportHandle = AnalysisReportHandler()
        self.__custemMenu = QMenu(self)
        self.__infoWindow = None
        self.__processWindow = None
        self.__selectiveWindow = None
        # Setup Ui Form from Ui_MainWindow
        self.__Ui = Ui_MainWindow()
        self.__my_map:dict = {}
        self.__Ui.setupUi(self)
        self.__precheck_server()
        self.__post_init_ui()
        # precheck the neccesities
        self.__precheck_server()
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
        path = self.__my_map[id(selected_item)]
        self.__image_holder.remove_by_paths([path])
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
        result = self.__on_handle_each_image_recognization(current_path)
        at = self.__on_handle_each_report_summon(current_path, result)
        logger.info("当前项报告生成完毕！")
        QMessageBox.information(self, f"当前项报告生成完毕！", "当前项报告生成完毕！请前往{at}查看")

    """
        open the selective window
    """
    def on_handle_selective_multi(self):
        if not self.__selectiveWindow:
            self.__selectiveWindow = SelectiveWindow(self.__image_holder.image_list())
            self.__selectiveWindow.onTellFetch.connect(self.__on_handle_given_multi)
        self.__selectiveWindow.show()


    """
        on start recognize the list items
    """
    def on_recognize_all_items_issue(self):
        lists_items = []
        count = self.__Ui.listWidget_selections.count() # 获取item的总数
        if count == 0:
            QMessageBox.critical(self, "请先导入图像!", "请先导入图像!")
            return
        
        for i in range(count):
            lists_items.append(self.__Ui.listWidget_selections.item(i)) # 获取每一个item
        item_text = []
        for item in lists_items:
            item_text.append(self.__image_holder.gain_paths_from_names([item.text()])[0]) 
            
        self.__on_recognize_lists_issue(item_text)

    def on_clear_all(self):
        self.__image_holder.clear()
        self.__on_change_the_ui_when_images_flash()

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
        logger.info("Report generation trying to start...")
        try:
            self.__analysisReportHandle.analysis_report()
        except Exception as e:
           logger.error(str(e))
           QMessageBox.critical(self, "发生错误！",
                                 "发生错误: " + str(e) + ", \n很有可能您正在打开待写入文件！请关闭后重试！")
        logger.info("Report generation done")
        QMessageBox.information(self, "报告生成完毕！", f"报告生成完毕，请查看: {self.__analysisReportHandle.gain_gen_path()}")

    def on_handling_audio_issue(self):
        if self.__audioServer.is_recording:
            self.__Ui.btn_audio_control.setText("开始录音")
            self.__audioServer.stop_recording()
        else:
            self.__Ui.btn_audio_control.setText("结束录音")
            self.__audioServer.start_recording()


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

    def __setup_logger(self):
        logger.add(sys.stdout, level="TRACE")

    def __on_handle_shutdown_audio_server(self):
        logger.info("Callback the shutdown")
        self.__Ui.btn_audio_control.setText("开始录音")

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
        self.__Ui.label_report_path.setText("报告生成路径位于: " + path)
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
        self.__Ui.label_analysis_report.setText("报告解析小程序位置: " + path)
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
            self.__Ui.label_display.clear()
            self.__browsing_guide.reset_as_clean()
        else:
            self.__browsing_guide.set_total_size(left_size)
 
        self.__my_map.clear()
        self.__Ui.listWidget_selections.clear()
        lists = self.__image_holder.image_list()
        for each_image in lists:
            item = QListWidgetItem(PathUtils.gain_name_from_path(each_image))
            self.__my_map[id(item)] = each_image
            self.__Ui.listWidget_selections.addItem(item)

    """
        on handle the each recognization
    """
    def __on_handle_each_image_recognization(self, image_path: str) -> bool:
        logger.info("开始此次识别")
        result = self.__model_handler.do_execute_check(image_path)
        logger.info(f"Current item check result is: {result}!")
        return result
        

    """
        handling the report issue
    """
    def __on_handle_each_report_summon(self, image_path: str, result: bool) -> str:
        save_at = self.__summonReportHandle.summon_report(image_path, not result)
        logger.info(f"报告生成在 {save_at}")
        self.tellSummonWhere.emit(save_at)
        return save_at

    """
        the post-initializations of the ui
    """
    def __post_init_ui(self):
        self.__Ui.toolBar.insertWidget(self.__Ui.action_prev_image, self.__browsing_guide)
        delete_action = QAction("删除选中项", self)
        self.__custemMenu.addAction(delete_action)
        delete_action.triggered.connect(self.on_handle_current_delete)
        self.__Ui.listWidget_selections.setContextMenuPolicy(Qt.CustomContextMenu)
    
    def __precheck_server(self):
        logger.info("Checking the runtime audio...")
        if not PathUtils.check_paths_if_exsit("Core/Audio/vosk-model-small-cn-0.22"):
            logger.error("Can not load the package model of audios...")
            self.__Ui.btn_audio_control.setEnabled(False)
        else:
            self.__audioServer = AudioServer()
            self.__audioServer.signal_tell_recognize.connect(self.__handling_callback_sound)
            self.__audioServer.signal_tell_shutdown.connect(self.__on_handle_shutdown_audio_server)
        logger.info("Checking the runtime audio done")



    def __show_audio_indications(self):
        QMessageBox.information(
            self, "语音指引", 
"清空操作：如果语音中包含“清空”字样，系统将执行清空操作。\
导入操作：当语音中包含“导入”时，系统会进一步判断导入的类型：\
文件夹导入：如果语音中提到“文件夹”，系统会允许用户选择文件夹进行导入。\
图片导入：如果语音中提到“图片”，用户可以选择单独导入图片。\
设置操作：当语音中包含“设置”字样时，系统将根据设置内容执行不同操作：\
生成路径设置：配置生成路径。\
模型设置：用户可以设置使用的模型。\
解析路径设置：配置解析路径。\
识别操作：如果语音中提到“识别”，系统将根据具体需求执行：\
识别全部：执行对所有项的识别。\
识别当前：执行当前项的识别。\
识别多张：执行多张图片的识别。\
查看操作：如果语音中包含“查看”，系统将执行查看相关操作。\
解析操作：如果语音中提到“解析”，系统会执行解析相关操作。")

    def __handling_callback_sound(self, info: str):
        logger.info(f"check the info: {info}")
        self.__Ui.label_soundinfo.setText(f"语音服务结果：{info}")

        if "清空" in info:
            logger.info("执行清空操作")
            self.on_clear_all()
        elif "导入" in info:
            if "文件夹" in info:
                logger.info("执行文件夹导入")
                self.on_loadImagesBySelectingFolders()
            elif "图片" in info:
                logger.info("执行选择导入")
                self.on_loadImagesBySelectingPaths()
        
        elif "设置" in info:
            if "生成路径" in info:
                logger.info("执行生成路径设置")
                self.on_handle_summon_path_set()
            elif "模型" in info:
                logger.info("执行模型设置")
                self.on_handle_model_import()
            elif "解析路径" in info:
                logger.info("执行解析路径设置")
                self.on_handle_analysis_path_set()

        elif "识别" in info:
            if "全部" in info:
                logger.info("执行识别全部")
                self.on_recognize_all_items_issue()
            elif "当前" in info:
                logger.info("执行识别当前")
                self.on_recognize_current_item_issue()
            elif "多张" in info:
                logger.info("执行识别多张")
                self.on_handle_selective_multi()  

        elif "查看" in info:
            logger.info("执行查看操作")
            self.on_handle_check()

        elif "解析" in info:
            logger.info("执行解析！")
            self.on_handle_analysis()
        


    def __init_connections(self):
        logger.trace("initializing the connections...")
        """toolbar and menubar actions connnections"""
        self.__Ui.action_import_folder.triggered.connect(self.on_loadImagesBySelectingFolders)
        self.__Ui.action_import_images.triggered.connect(self.on_loadImagesBySelectingPaths)
        self.__Ui.action_next_image.triggered.connect(self.on_switch_next_image)
        self.__Ui.action_prev_image.triggered.connect(self.on_switch_prev_image)     
        self.__Ui.action_import_models.triggered.connect(self.on_handle_model_import)
        self.__Ui.action_check_infos.triggered.connect(self.on_handle_check)
        self.__Ui.action_summon_report_for_all.triggered.connect(self.on_recognize_all_items_issue)
        self.__Ui.action_summon_report_for_current.triggered.connect(self.on_recognize_current_item_issue)
        self.__Ui.action_summon_selectMulti.triggered.connect(self.on_handle_selective_multi)
        self.__Ui.action_analysis_report.triggered.connect(self.on_handle_analysis)
        self.__Ui.action_clear.triggered.connect(self.on_clear_all)
        """
            list widget ui
        """
        self.__Ui.listWidget_selections.itemClicked.connect(self.__on_item_clicked)
        self.__Ui.listWidget_selections.customContextMenuRequested.connect(self.__onshowCustomizeMenu)
        
        """
            other part of ui
        """
        self.__browsing_guide.postIndex.connect(self.on_switch_given_index_image)
        self.__Ui.btn_set_analysis_path.clicked.connect(self.on_handle_analysis_path_set)
        self.__Ui.btn_set_summon_path.clicked.connect(self.on_handle_summon_path_set)
        self.__Ui.btn_summon_report_for_current.clicked.connect(self.on_recognize_current_item_issue)
        self.__Ui.btn_analysis_report.clicked.connect(self.on_handle_analysis)
        self.__Ui.btn_summon_report_for_all.clicked.connect(self.on_recognize_all_items_issue)
        self.__Ui.btn_summon_select_multi.clicked.connect(self.on_handle_selective_multi)
        self.__Ui.btn_audio_control.clicked.connect(self.on_handling_audio_issue)
        self.__Ui.btn_check_indications.clicked.connect(self.__show_audio_indications)
    """
        handling the item clicked
    """
    def __on_item_clicked(self, item: QListWidgetItem):
        logger.trace(f"item clicked! item text: {item.text()}")
        path = self.__my_map[id(item)]
        logger.trace(f"will handle the path: {path}")
        self.__load_image_work(path)

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
        self.__Ui.btn_summon_select_multi.setEnabled(enabled)
        self.__Ui.action_summon_report_for_all.setEnabled(enabled)
        self.__Ui.action_summon_report_for_current.setEnabled(enabled)
        self.__Ui.action_summon_selectMulti.setEnabled(enabled)

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

    """
        issuing the items lists
    """
    def __set_stop(self):
        self.__shell_terminate = True

    def __on_recognize_lists_issue(self, image_lists: list[str]):

        enabled :bool = \
            self.__image_holder.image_list_size() != 0 and \
                self.__model_handler.holding_model != "" and \
                self.__summonReportHandle.summon_folder != ""
        if not enabled:
            QMessageBox.critical(self, "不允许进行识别", "不允许进行识别, 请检查是否导入图像, 模型和设置生成路径！")
            return

        if self.__processWindow is None:
            self.__processWindow = ProcessingWindow()
            self.tellSummonWhere.connect(self.__processWindow.handle_report_summon_where)
            self.tellResultHow.connect(self.__processWindow.handle_result)
            self.__processWindow.tellStopCurrentIssue.connect(self.__set_stop)
            self.__processWindow.tellSummonReport.connect(self.__on_continue_summon_report)
            
        self.__processWindow.current_handling_tol = len(image_lists)
        self.__processWindow.current_handling_summon = 0
        self.__processWindow.current_handling_reco = 0
        self.__processWindow.show()
        self.__shell_terminate = False
        index = 0
        self.__cached_result = []
        self.__cached_images = image_lists
        for image in image_lists:
            if self.__shell_terminate:
                logger.trace("threads are terminated due to the user")
                return
            QApplication.processEvents()
            this_res = self.__on_handle_each_image_recognization(image)
            self.__cached_result.append(this_res)
            index += 1
            self.__processWindow.current_handling_reco = index
            logger.trace(f"finish: {index}'s recognizations")
            self.tellResultHow.emit(f"完成对第{index}图像{image}的检查, 结果为{this_res}")
        logger.trace("finish recognization")
        self.__processWindow.onHandleTheReadynessOfSummon()

    def __on_continue_summon_report(self):   
        index: int = 0
        for each_image, each_result in zip(self.__cached_images, self.__cached_result):
            if self.__shell_terminate:
                return
            QApplication.processEvents()
            self.__on_handle_each_report_summon(each_image, each_result)
            index += 1
            self.__processWindow.current_handling_summon = index
        QMessageBox.information(self, "生成报告完成", f"生成报告完成，请在{self.__summonReportHandle.summon_folder}文件夹下查询！")

    """
        on handle the selective multi
    """
    def __on_handle_given_multi(self):
        paths = self.__selectiveWindow.fetch_result()
        if len(paths) == 0:
            return
        self.__on_recognize_lists_issue(paths)
