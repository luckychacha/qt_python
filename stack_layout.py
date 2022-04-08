#!/usr/local/bin/python3
#-*- coding: UTF-8 -*-

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QStackedLayout,
    QApplication,
    QLabel,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTabWidget
)
from layout_color_widget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.vertical_layout = QVBoxLayout()
        
        self.horizontally_layout = QHBoxLayout()
        
        # stack
        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(Color("red"))
        self.stack_layout.addWidget(Color("yellow"))
        self.stack_layout.addWidget(Color("blue"))
        
        
        # button
        # red_button = QPushButton("red")
        # red_button.pressed.connect(self.red_button_pressed)
        # yellow_button = QPushButton("yellow")
        # yellow_button.pressed.connect(self.yellow_button_pressed)
        # blue_button = QPushButton("blue")
        # blue_button.pressed.connect(self.blue_button_pressed)

        # self.horizontally_layout.addWidget(red_button)
        # self.horizontally_layout.addWidget(yellow_button)
        # self.horizontally_layout.addWidget(blue_button)
        
        # 此处使用 QTabWidget 代替按钮和 Color
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabPosition(QTabWidget.East)
        self.tab_widget.setMovable(True)
        for idx, desc in enumerate(["red", "yellow", "blue"]):
            self.tab_widget.addTab(Color(desc), desc)
        self.tab_widget.currentChanged.connect(self.tab_changed)
        self.tab_widget.setDocumentMode(True)
        
        self.horizontally_layout.addWidget(self.tab_widget)
        
        # main layout
        self.vertical_layout.addLayout(self.stack_layout)
        self.vertical_layout.addLayout(self.horizontally_layout)
        
        widget = QWidget()
        widget.setLayout(self.vertical_layout)
        self.setCentralWidget(widget)
    
    def tab_changed(self):
        # self.stack_layout.setCurrentIndex(self.tab_widget.currentIndex())
        self.stack_layout.setCurrentIndex(self.tab_widget.currentIndex())
            
    
    def red_button_pressed(self):
        self.stack_layout.setCurrentIndex(0)
        
    def yellow_button_pressed(self):
        self.stack_layout.setCurrentIndex(1)

    def blue_button_pressed(self):
        self.stack_layout.setCurrentIndex(2)

        
    
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()