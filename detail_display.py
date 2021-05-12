from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot

from image_viewer import ImageViewer

class DetailDisplay(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        # create widget layout
        self.__layout = QtWidgets.QVBoxLayout()
        
        # create table widget
        self.__detailWidget = QtWidgets.QTableWidget()
        self.setup_detailWidget()
        self.__detailWidget.showGrid = True

        self.setup_DetailDisplay()
    
    def setup_detailWidget(self):
        self.__detailWidget.showGrid = True # show table grids

        # create columns
        column_names = ["Source", "Time", "Image Location"]
        for col_number in range(0, len(column_names)):
            self.__detailWidget.insertColumn(col_number)
        self.__detailWidget.setHorizontalHeaderLabels(column_names)

        # set size adjustment policy
        self.__detailWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.__detailWidget.resizeColumnsToContents()
        self.__detailWidget.horizontalHeader().setStretchLastSection(True)

        # set alternating row colors
        self.__detailWidget.setAlternatingRowColors(True)
        self.__detailWidget.setStyleSheet("QTableWidget { alternate-background-color: #e2bcb7;background-color: #b67162; border : 2px solid black; }")
        
        # set widget max size
        self.__detailWidget.setMaximumWidth(500)

        # connect detail display cells to cellClicked event
        self.__detailWidget.cellDoubleClicked.connect(self.cell_double_clicked)

    def setup_DetailDisplay(self):
        self.__layout.addWidget(self.__detailWidget)
        self.setLayout(self.__layout)
        self.setStyleSheet("QWidget"
                            "{"
                            "border : 2px solid black;"
                            "background : #b67162;"
                            "}")

    
    # write details when new alert is triggered
    @pyqtSlot(str,str,str)
    def rx_write_details(self, filepath, timestamp, stream_num):
        rowPosition = self.__detailWidget.rowCount()
        # print(rowPosition)
        self.__detailWidget.insertRow(rowPosition)
        self.__detailWidget.setItem(rowPosition,2,QtWidgets.QTableWidgetItem(filepath))
        self.__detailWidget.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(timestamp))
        self.__detailWidget.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(stream_num))
        self.__detailWidget.resizeColumnToContents(1)

    def cell_double_clicked(self, row, column):
        filepath = self.__detailWidget.item(row,column).text()
        if column == 2:
            timestamp = self.__detailWidget.item(row,column-1).text()
            # print(f"you have clicked on {filepath}")
            self.viewer = ImageViewer(filepath,timestamp)
            self.viewer.view()
