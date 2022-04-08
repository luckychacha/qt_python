#!/usr/local/bin/python3
#-*- coding: UTF-8 -*-

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGridLayout, QApplication, QWidget, QMainWindow
import sys

from matplotlib.widgets import Widget

from layout_color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        grid_layout = QGridLayout()
        grid_layout.addWidget(Color("red"), 0, 0)
        grid_layout.addWidget(Color("green"), 1, 1)
        grid_layout.addWidget(Color("yellow"), 4, 2)
        
        widget = QWidget()
        widget.setLayout(grid_layout)
        self.setCentralWidget(widget)
        

app = QApplication(sys.argv)

main = MainWindow()
main.show()

app.exec()