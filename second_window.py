# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestUI2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1209, 654)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_bar = QtWidgets.QFrame(self.centralwidget)
        self.side_bar.setMaximumSize(QtCore.QSize(100, 16777215))
        self.side_bar.setStyleSheet("border: 2px solid #e7e7e7")
        self.side_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_bar.setObjectName("side_bar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.side_bar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menu = QtWidgets.QFrame(self.side_bar)
        self.menu.setMinimumSize(QtCore.QSize(80, 50))
        self.menu.setMaximumSize(QtCore.QSize(80, 45))
        self.menu.setStyleSheet("border: none;\n"
"")
        self.menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu.setObjectName("menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.menu)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.menu_label = QtWidgets.QLabel(self.menu)
        self.menu_label.setMinimumSize(QtCore.QSize(80, 0))
        self.menu_label.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.menu_label.setFont(font)
        self.menu_label.setStyleSheet("border: none;")
        self.menu_label.setAlignment(QtCore.Qt.AlignCenter)
        self.menu_label.setObjectName("menu_label")
        self.verticalLayout_4.addWidget(self.menu_label)
        self.verticalLayout.addWidget(self.menu, 0, QtCore.Qt.AlignLeft)
        self.func = QtWidgets.QFrame(self.side_bar)
        self.func.setMinimumSize(QtCore.QSize(80, 0))
        self.func.setMaximumSize(QtCore.QSize(80, 16777215))
        self.func.setStyleSheet("border: none;")
        self.func.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.func.setFrameShadow(QtWidgets.QFrame.Raised)
        self.func.setObjectName("func")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.func)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.func_child = QtWidgets.QFrame(self.func)
        self.func_child.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.func_child.setFrameShadow(QtWidgets.QFrame.Raised)
        self.func_child.setObjectName("func_child")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.func_child)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.func_child)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"  background-color: white; \n"
"  color: black; \n"
"  border: 2px solid #4CAF50;\n"
"  padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #4CAF50;\n"
"  color: white;\n"
"  padding: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: white; \n"
"  color: black; \n"
"  border: 2px solid #4CAF50;\n"
"  padding: 8px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.func_child)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"  background-color: white; \n"
"  color: black; \n"
"  border: 2px solid #008CBA;\n"
"  padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #008CBA;\n"
"  color: white;\n"
"padding: 8px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: white; \n"
"  color: black; \n"
"  border: 2px solid #008CBA;\n"
"  padding: 8px;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.func_child)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("\n"
"QPushButton {\n"
"  background-color: white; \n"
"  color: black; \n"
"  border: 2px solid #f44336;\n"
"  padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f44336;\n"
"  color: white;\n"
"  padding: 8px;\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: white; \n"
"  color: black; \n"
"  border: 2px solid #f44336;\n"
"  padding: 8px;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_3.addWidget(self.func_child)
        self.verticalLayout.addWidget(self.func, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.side_bar, 0, QtCore.Qt.AlignLeft)
        self.dis_window = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dis_window.sizePolicy().hasHeightForWidth())
        self.dis_window.setSizePolicy(sizePolicy)
        self.dis_window.setMinimumSize(QtCore.QSize(1080, 607))
        self.dis_window.setMaximumSize(QtCore.QSize(99999, 16777215))
        self.dis_window.setStyleSheet("border: 2px solid #e7e7e7")
        self.dis_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dis_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dis_window.setObjectName("dis_window")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dis_window)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.dis_window)
        self.label.setMaximumSize(QtCore.QSize(1080, 607))
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.horizontalLayout.addWidget(self.dis_window)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_label.setText(_translate("MainWindow", "Menu"))
        self.pushButton.setText(_translate("MainWindow", "#1"))
        self.pushButton_2.setText(_translate("MainWindow", "#2"))
        self.pushButton_3.setText(_translate("MainWindow", "#3"))

