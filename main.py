from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
import sys
from dashboard import dashboard

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    db = dashboard()
    db.show()
    app.exec()