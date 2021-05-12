from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot

class ControlPanel(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.__panel_layout = QtWidgets.QGridLayout()
        
        self.toggle_monitor_button = QtWidgets.QPushButton()
        self.toggle_monitor_button.setText("Start")

        # connect toggle monitor button to slot
        self.toggle_monitor_button.clicked.connect(self.rx_toggle)

        self.setup_controlPanel()

    def setup_controlPanel(self):
        self.__panel_layout.addWidget(self.toggle_monitor_button)
        self.setLayout(self.__panel_layout)
        self.setMaximumHeight(200)
        self.setStyleSheet("QWidget"
                            "{"
                            "border : 2px solid black;"
                            "background : #b67162;"
                            "}")

    def rx_toggle(self):
        if self.toggle_monitor_button.text() == "Start":
            self.toggle_monitor_button.setText("Stop")
        else:
            self.toggle_monitor_button.setText("Start")
