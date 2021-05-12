from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from thumbnail_display import ThumbnailDisplay
from detail_display import DetailDisplay
from control_panel import ControlPanel

from handler import Handler
from watcher import Watcher

class dashboard(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.__windowTitle = "Firepost VA"
        self.__defaultSize = QtCore.QSize(1080,720)

        self.thumbnailDisplay = ThumbnailDisplay()

        self.detailDisplay = DetailDisplay()

        self.controlPanel = ControlPanel()

        self.handler = Handler()
        self.watcher = Watcher(["./stream_0"], self.handler)

        # connect handler to thumbnail display
        self.handler.tx_sendpathtime.connect(self.watcher.SendImage)
        self.watcher.sendImage.connect(self.thumbnailDisplay.rx_put_thumbnail)
        self.setup_mainWidget()
        
        # connect handler to detail display
        self.handler.tx_sendpathtime.connect(self.detailDisplay.rx_write_details)
        
        # connect controlPanel button to watcher
        self.controlPanel.toggle_monitor_button.clicked.connect(self.watcher.rxToggleObserver)

        # this should be the last step
        self.setup_dashboard()
    
        # self.watcher.run()
        
    def setup_mainWidget(self):
        self.__mainWidget = QtWidgets.QWidget()
        self.__mainWidget.setStyleSheet("QWidget"
                                        "{"
                                        "border : 2px solid black;"
                                        "background : #9e9d89;"
                                        "}")

        self.__mainWidget_layout = QtWidgets.QVBoxLayout()
        
        # add control bar at the top
        self.__mainWidget_layout.addWidget(self.controlPanel)

        # add other widgets here
        
        ## add in thumbnail display
        self.__bottom_layout = QtWidgets.QHBoxLayout()
        self.__bottom_layout.addWidget(self.thumbnailDisplay)
        
        ## add in detail display
        self.__bottom_layout.addWidget(self.detailDisplay)
        self.__mainWidget_layout.addLayout(self.__bottom_layout)

        # set main widget layout
        self.__mainWidget.setLayout(self.__mainWidget_layout)
    
    def setup_dashboard(self):
        # set window title
        self.setWindowTitle(self.__windowTitle)
        # set minimum window size
        self.setMinimumSize(self.__defaultSize)
        # set main widget
        self.setCentralWidget(self.__mainWidget)
    
    @staticmethod
    def create_placeholder(width, height, fill_color = "#e4d3cf"):
        placeholder_widget = QtWidgets.QFrame()
        placeholder_widget.setMaximumSize(width,height)
        placeholder_widget.setSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        placeholder_widget.setLineWidth(5)
        placeholder_widget.setStyleSheet("QWidget"
                                        "{"
                                        "border : 2px solid black;"
                                        f"background : {fill_color};"
                                        "}")
        return placeholder_widget

        
        