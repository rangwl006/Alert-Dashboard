from PyQt5 import QtCore, QtGui, QtWidgets

class ImageViewer(QtWidgets.QWidget):

    def __init__(self, image_path, timestamp):
        super().__init__()

        self.__defaultSize = QtCore.QSize(960,540)
        
        # image viewer layout
        self.__mainLayout = QtWidgets.QHBoxLayout()

        # setup qlabel to store image data
        self.__imageView = QtWidgets.QLabel()
        self.__imageView.setScaledContents(True) # enable image scaling

        # set image pixmap into qlabel
        self.set_image(image_path)

        # setup main image viewer
        self.__mainLayout.addWidget(self.__imageView)
        self.setLayout(self.__mainLayout)

    def set_image(self, image_path):
        image = QtGui.QPixmap(image_path)
        image = image.scaled(self.__defaultSize)
        self.__imageView.setPixmap(image)

    def view(self):
        self.show()