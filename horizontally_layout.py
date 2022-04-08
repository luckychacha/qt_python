#!/usr/local/bin/python3
#-*- coding: UTF-8 -*-
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget

from layout_color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self,):
        super().__init__()
        
        self.setWindowTitle("Horizontally Layout")
        layout = QHBoxLayout()
        
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()