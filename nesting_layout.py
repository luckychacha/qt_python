#!/usr/local/bin/python3
#-*- coding: UTF-8 -*-
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QMainWindow,
    QWidget
)

from layout_color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Nesting Layout")
        
        horizontally_layout = QHBoxLayout()
        vertical_layout_1 = QVBoxLayout()
        vertical_layout_2 = QVBoxLayout()
        
        horizontally_layout.setContentsMargins(0, 0, 0, 0)
        horizontally_layout.setSpacing(20)
        
        vertical_layout_1.addWidget(Color("red"))
        vertical_layout_1.addWidget(Color("green"))
        vertical_layout_1.addWidget(Color("yellow"))
        
        vertical_layout_2.addWidget(Color("grey"))
        vertical_layout_2.addWidget(Color("black"))
        
        horizontally_layout.addLayout(vertical_layout_1)
        horizontally_layout.addWidget(Color("green"))
        horizontally_layout.addLayout(vertical_layout_2)
        
        widget = QWidget()
        widget.setLayout(horizontally_layout)
        
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()