from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from image_viewer import ImageViewer

class ThumbnailDisplay(QtWidgets.QWidget):
    
    tx_showViewer = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.__layout = QtWidgets.QVBoxLayout()
        self.__display_area = QtWidgets.QListWidget()
        
        self.setup_display_area()
        self.setup_ThumbnailDisplay()

        # connect thumbnail display to displaying viewer
        self.__display_area.itemDoubleClicked.connect(self.rx_thumbnail_double_clicked)

    def setup_display_area(self):
        self.__display_area.alternatingRowColors = True
        self.__display_area.setMaximumWidth(500)    
        self.__display_area.layoutDirection = QtCore.Qt.LayoutDirection.LeftToRight
        self.__display_area.setGridSize(QtCore.QSize(100,100)) 
        self.__display_area.setViewMode(QtWidgets.QListView.ViewMode.IconMode)
        self.__display_area.setIconSize(QtCore.QSize(85,40)) 
        self.__display_area.setTextElideMode(QtCore.Qt.TextElideMode.ElideMiddle)
        self.__display_area.setAutoScroll(True)

    def setup_ThumbnailDisplay(self):
        
        self.__layout.addWidget(self.__display_area)
        self.setLayout(self.__layout)
        self.setStyleSheet("QWidget"
                            "{"
                            "border : 2px solid black;"
                            "background : #b67162;"
                            "}")

    def rx_put_thumbnail(self, image, timestamp, image_path):
        # print(f"putting thumbnail of {image_path}")
        img = QtGui.QIcon(image)
        thumbnail = QtWidgets.QListWidgetItem(img, timestamp)
        thumbnail_font = QtGui.QFont()
        thumbnail_font.setPointSizeF(5.5)
        thumbnail.setFont(thumbnail_font)
        thumbnail.setWhatsThis(image_path)
        thumbnail.setTextAlignment(64)
        self.__display_area.addItem(thumbnail)
        
    def rx_thumbnail_double_clicked(self, item):
        image_path = item.whatsThis()
        image_timestamp = item.text()
        self.viewer = ImageViewer(image_path, image_timestamp)
        self.viewer.view()