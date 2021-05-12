import sys, time, json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

DEBUG = False

class Watcher(QObject):
    sendImage = pyqtSignal(QtGui.QPixmap, str, str)

    def __init__(self, directory_list, handler, level=None, *args, **kwargs):
        QObject.__init__(self, parent=None)

        self.observers = []
        self.directory_list = directory_list
        self.observer_state = False
        self.event_handler = handler

    def run(self):
        if self.observer_state == True:

            if not DEBUG: print("Watching folders")

            # reset the number of observers each time the function is called again
            self.observers = []
            for directory in self.directory_list:
                self.observers.append(Observer())

            print(self.directory_list)
            for observer in self.observers:
                i = self.observers.index(observer)    
                observer.schedule(self.event_handler, self.directory_list[i], recursive=True)

            for observer in self.observers:
                if not DEBUG: print("running")
                observer.daemon = True
                observer.start()
        
        else:
            if not DEBUG: print("Stopped watching folders...")
            for observer in self.observers:
                observer.stop()

            observer.join()

    def rxToggleObserver(self):
        if not DEBUG: print("clicked")
        self.observer_state = not self.observer_state
        if self.observer_state == True:
            if not DEBUG: print("on")
            self.run()
        if self.observer_state == False:
            if not DEBUG: print("off")
            self.run()

    @pyqtSlot(str, str, str)
    def SendImage(self, image_path, timestamp, camera_ip):
        if not DEBUG: print("image received")
        icon_width = 85
        icon_height = 40
        image = QtGui.QPixmap(image_path)
        image.scaled(icon_width,icon_height,1)
        self.sendImage.emit(image, timestamp, image_path)

if __name__=='__main__':
    pass