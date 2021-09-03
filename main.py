from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys
import main_window
import second_window
import threading
import time

app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")
MainWindow = QtWidgets.QMainWindow()
ui = main_window.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

def window_1_btn_1():
    pixmap = QPixmap("pic.png")
    pixmap_2 = QPixmap("pic2.png")
    ui.label.setScaledContents(True)
    ui.label.setPixmap(pixmap)
    ui.label.repaint()
    ui.label_2.setScaledContents(True)
    ui.label_2.setPixmap(pixmap_2)
    ui.label_2.repaint()

def window_1_btn_2():
    pixmap = QPixmap("pic2.png")
    pixmap_2 = QPixmap("pic.png")
    ui.label.setScaledContents(True)
    ui.label.setPixmap(pixmap)
    ui.label.repaint()
    ui.label_2.setScaledContents(True)
    ui.label_2.setPixmap(pixmap_2)
    ui.label_2.repaint()

def window_2_btn_3():
    ui = second_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

ui.pushButton.clicked.connect(window_1_btn_1)
ui.pushButton_2.clicked.connect(window_1_btn_2)
ui.pushButton_3.clicked.connect(window_2_btn_3)

sys.exit(app.exec_())
