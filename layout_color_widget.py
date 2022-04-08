#!/usr/local/bin/python3
#-*- coding: UTF-8 -*-
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QWidget

class Color(QWidget):
    def __init__(self, color) -> None:
        super().__init__()
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)