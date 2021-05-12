import sys, time, json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot

DEBUG = False 

def getStreams(filepath = "va_config.json"):
    global DEBUG
    with open(filepath, 'r') as file:
        cfg = json.load(file)
        streams = cfg["polcam_url"]
        num_streams = len(streams)
        stream_names = list()
        for stream in range(0,num_streams):
            stream_names.append(f'stream_{str(stream)}')
        stream_dict = dict(zip(stream_names, streams))
        if not DEBUG: print(stream_dict)
    return stream_dict

class Handler(FileSystemEventHandler, QObject):

    tx_sendpathtime = pyqtSignal(str,str,str)
    tx_playsound = pyqtSignal()

    def __init__(self):
        FileSystemEventHandler.__init__(self)
        QObject.__init__(self, parent = None)
        self.timestamp = None
        self.streams = getStreams()

    def on_any_event(self, event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            try:
                filename = event.src_path
                if not DEBUG: print(f'file: {filename}')
                stream_name = "Unknown"
                for stream in self.streams:
                    if stream in filename:
                        if not DEBUG: print(f'file belongs to: {stream}')
                        stream_name = self.streams[stream]
                        if not DEBUG: print("Camera number: {}".format(stream))
                    # else:
                    #     print("Camera number: {}".format(stream_name))
            
                time.sleep(1) # let the file get fully written before doing anything else
                self.timestamp = QtCore.QDateTime().currentDateTime().toString()
                self.tx_sendpathtime.emit(filename, self.timestamp, stream_name)
                # self.txplaysound.emit()
                if not DEBUG: print("Event: {0}".format(filename))
            except:
                print("Unkown file type added")


if __name__=='__main__':
    getStreams()