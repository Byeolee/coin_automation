import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import pykorbit

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(100, 200, 300, 400)
#         self.setWindowTitle("PyQt")
#         self.setWindowIcon(QIcon("icon.png"))
#
#         btn1 = QPushButton("button 1", self)
#         btn2 = QPushButton("button 2", self)
#         btn2.move(10, 20)
#
#         btn1.clicked.connect(self.btn_clicked)
#
#     def btn_clicked(self):
#         print("버튼1 클릭")

form_class = uic.loadUiType("mywindow.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("버튼1 클릭")

app = QApplication(sys.argv)
window = MyWindow()
window.show()

app.exec_()