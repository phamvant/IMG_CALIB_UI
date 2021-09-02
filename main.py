from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
import sys
import main_window as wi
import window2
import threading
import time

app = QtWidgets.QApplication(sys.argv)
app.setStyle("Fusion")
MainWindow = QtWidgets.QMainWindow()

# def main_UI():
ui = wi.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
def display():
    pixmap = QPixmap("pic.png")
    pixmap_2 = QPixmap("pic2.png")
    ui.label.setScaledContents(True)
    ui.label.setPixmap(pixmap)
    ui.label.repaint()
    ui.label_2.setScaledContents(True)
    ui.label_2.setPixmap(pixmap_2)
    ui.label_2.repaint()
    ui.pushButton_2.clicked.connect(display_2)

def display_2():
    ui.label.setScaledContents(True)
    pixmap = QPixmap("pic2.png")
    ui.label.setPixmap(pixmap)
    ui.label.repaint()
    ui.label_2.setScaledContents(True)
    pixmap_2 = QPixmap("pic.png")
    ui.label_2.setPixmap(pixmap_2)
    ui.label_2.repaint()
ui.pushButton.clicked.connect(display)
# ui.pushButton_2.clicked.connect(display_2)

# def calcTotal(self):
#     # print("Name: ", self.lineEdit.text())
#     msg = QtWidgets.QMessageBox()
#     msg.setWindowTitle("Thông tin")
#     msg.setText("Tên của bạn là: {}".format(self.lineEdit.text()))
#     msg.setInformativeText("Giới tính của bạn là: {}!".format("Đực" if self.comboBox.currentText() == "Male" else "Cái"))
#     msg.exec_()

def count():
    for i in range(999):
        print(i)
        time.sleep(0.5)

sys.exit(app.exec_())
