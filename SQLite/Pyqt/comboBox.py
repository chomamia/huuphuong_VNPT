from curses import window
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Python")
        # setting geometry
        self.setGeometry(100, 100, 600, 400)
        # calling method
        self.UiCompoments()
        self.show()
    def UiCompoments(self):
        # creating a combo box widget
        self.combo_box = QComboBox(self)
        # setting geometry  of combo box 
        self.combo_box.setGeometry(200, 150, 120, 30)
        # geek list
        geek_list = ["Geek", "Geeky Geek", "Legend Geek", "Ultra Legend Geek"]
        # adding list of iteam to combo box
        self.combo_box.addItems(geek_list)
        # creating a editable combo box
        self.combo_box.setEditable(True)
# create pyqt5 app 
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
    