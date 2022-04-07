from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QComboBox, QListWidget, QSpinBox, QDoubleSpinBox, QSlider, QDial
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
# Only needed for access to command line arguments
import sys

window_titles = [
    'a',
    'b',
    'c',
    'd',
    'e'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0
        
        self.setWindowTitle(self.get_window_title())
        
        # 文本框
        self.label = QLabel()
        font = self.label.font()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        # input 输入框
        self.input = QLineEdit()
        self.input.setPlaceholderText("请输入任意内容！")
        # 输入模型
        # self.input.setInputMask("000.000.000.000;_")
        self.input.textChanged.connect(self.label.setText)
        
        # 按钮
        self.button = QPushButton("Push Me".format(self.count))
        self.button.setCheckable(True)
        self.input.textChanged.connect(self.button.setText)
        
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_togged)
        
        # 图片
        self.image = QLabel()
        self.image.setPixmap(QPixmap("otje.jpg"))
        self.image.setScaledContents(True)
        
        # 下拉框
        self.comboBox = QComboBox()
        self.comboBox.addItems(["一", "二", "三"])
        self.comboBox.currentIndexChanged.connect(self.combo_box_index_changed)
        self.comboBox.currentTextChanged.connect(self.combo_box_text_changed)
        self.comboBox.setEditable(True)
        
        # list
        self.list = QListWidget()
        self.list.addItems(["列表1", "列表2", "列表3"])
        self.list.currentItemChanged.connect(self.list_item_changed)
        self.list.currentTextChanged.connect(self.list_text_changed)

        # spinbox 微调框
        # QSpinBox 只支持整数 QDoubleSpinBox 支持浮点数
        self.spinBox = QDoubleSpinBox()
        self.spinBox.setMaximum(10.0)
        self.spinBox.setMinimum(-10.0)
        # self.spinBox.setSingleStep(0.1)
        self.spinBox.setSingleStep(0.1)
        self.spinBox.setPrefix("前缀：")
        self.spinBox.setSuffix("后缀。")
        self.spinBox.valueChanged.connect(self.spin_box_value_changed)
        self.spinBox.textChanged.connect(self.spin_box_text_changed)

        # slider 滑块
        self.slider = QSlider()
        # self.slider.setMaximum(10)
        # self.slider.setMinimum(-10)
        self.slider.setRange(-10, 11)
        self.slider.setSingleStep(0.1)
        
        self.slider.sliderMoved.connect(self.slider_moved)
        self.slider.valueChanged.connect(self.slider_value_changed)
        self.slider.sliderPressed.connect(self.slider_pressed)
        self.slider.sliderReleased.connect(self.slider_released)
        
        # QDial
        self.dial = QDial()
        self.dial.setRange(-10, 100)
        self.dial.setSingleStep(0.5)

        self.dial.valueChanged.connect(self.dial_value_changed)
        self.dial.sliderMoved.connect(self.dial_slider_position)
        self.dial.sliderPressed.connect(self.dial_slider_pressed)
        self.dial.sliderReleased.connect(self.dial_slider_released)

        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.image)
        layout.addWidget(self.comboBox)
        layout.addWidget(self.list)
        layout.addWidget(self.spinBox)
        layout.addWidget(self.slider)
        layout.addWidget(self.dial)
        
        container = QWidget()
        container.setLayout(layout)
        
        
        self.windowTitleChanged.connect(self.the_window_title_was_changed)
        
        self.setCentralWidget(container)
    
    def the_button_was_clicked(self):
        self.count += 1
        print("Clicked {} Times!".format(self.count))
        # self.button.setEnabled(False)
        self.setWindowTitle(self.get_window_title())
    
    def the_button_was_togged(self, checked):
        print("Checked?")
    
    def the_window_title_was_changed(self, window_title):
        print("window title was changed: {}".format(window_title))
    
    def get_window_title(self):
        return window_titles[self.count % len(window_titles)]
    
    def combo_box_index_changed(self, index):
        print("index: {}".format(index))
    def combo_box_text_changed(self, text):
        print("text: {}".format(text))
        
    def list_item_changed(self, item):
        print("list item changed: {} index: {}".format(item, self.list.currentIndex))
    def list_text_changed(self, text):
        print("list text changed: {}".format(text))
        
    def spin_box_value_changed(self, value):
        print("spin_box_value_changed: {}".format(value))
    def spin_box_text_changed(self, text):
        print("spin_box_text_changed: {}".format(text))
        
    # slider
    def slider_moved(self, slider_moved):
        print("slider_moved: {}".format(slider_moved))
    def slider_value_changed(self, slider_value_changed):
        print("slider_value_changed: {}".format(slider_value_changed))
    def slider_pressed(self, slider_pressed):
        print("slider_pressed: {}".format(slider_pressed))
    def slider_released(self, slider_released):
        print("slider_released: {}".format(slider_released))

    # qdial
    def dial_value_changed(self, i):
        print(i)

    def dial_slider_position(self, p):
        print("position", p)

    def dial_slider_pressed(self):
        print("Pressed!")

    def dial_slider_released(self):
        print("Released")
        
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.
app.exec()