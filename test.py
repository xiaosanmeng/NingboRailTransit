#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Time : 2021/5/13 
# @Author : XIAO
# @File : test.py
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
                             QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,
                             QGridLayout,
                             QLineEdit)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication


# ##***工具栏***## #
# ##***绝对定位***## #
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5. QtWidgets import *
from utils import *

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 722)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 491, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 40, 461, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_14 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 0, 2, 1, 1)
        self.pushButton_line = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pushButton_line.setFont(font)
        self.pushButton_line.setObjectName("pushButton_line")
        self.gridLayout.addWidget(self.pushButton_line, 1, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 2, 1, 1)
        self.pushButton_navi = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pushButton_navi.setFont(font)
        self.pushButton_navi.setObjectName("pushButton_navi")
        self.gridLayout.addWidget(self.pushButton_navi, 2, 0, 1, 1)
        self.pushButton_station = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pushButton_station.setFont(font)
        self.pushButton_station.setObjectName("pushButton_station")
        self.gridLayout.addWidget(self.pushButton_station, 0, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 260, 361, 155))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(410, 250, 341, 251))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.layoutWidget2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox.setObjectName("checkBox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 540, 731, 131))
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_3.setBuddy(self.comboBox)
        self.label_4.setBuddy(self.lineEdit_3)
        self.label_5.setBuddy(self.lineEdit_2)
        self.label_2.setBuddy(self.lineEdit)
        self.label_6.setBuddy(self.lineEdit)
        self.label_7.setBuddy(self.comboBox)
        self.label_9.setBuddy(self.lineEdit_2)
        self.label_8.setBuddy(self.lineEdit_3)
        self.label_10.setBuddy(self.lineEdit)
        self.label_11.setBuddy(self.lineEdit)
        self.label_12.setBuddy(self.lineEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "宁波轨道交通乘车查询系统"))
        self.pushButton_14.setText(_translate("MainWindow", "公交卡办理"))
        self.pushButton_line.setText(_translate("MainWindow", "路线查询"))
        self.pushButton_11.setText(_translate("MainWindow", "公交卡充值"))
        self.pushButton_navi.setText(_translate("MainWindow", "导航查询"))
        self.pushButton_station.setText(_translate("MainWindow", "站点查询"))
        self.pushButton_12.setText(_translate("MainWindow", "公交卡乘车"))
        self.label_3.setText(_translate("MainWindow", "路线："))
        self.comboBox.setItemText(0, _translate("MainWindow", "1号线"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2号线"))
        self.comboBox.setItemText(2, _translate("MainWindow", "3号线"))
        self.comboBox.setItemText(3, _translate("MainWindow", "4号线"))
        self.label_4.setText(_translate("MainWindow", "起始站:"))
        self.label_5.setText(_translate("MainWindow", "终点站:"))
        self.label_2.setText(_translate("MainWindow", "站点:"))
        self.label_6.setText(_translate("MainWindow", "身份证号："))
        self.label_7.setText(_translate("MainWindow", "是否优惠卡："))
        self.checkBox.setText(_translate("MainWindow", "优惠卡"))
        self.label_9.setText(_translate("MainWindow", "身份证号查询："))
        self.label_8.setText(_translate("MainWindow", "卡号查询:"))
        self.label_10.setText(_translate("MainWindow", "乘车卡号："))
        self.label_11.setText(_translate("MainWindow", "乘车起点："))
        self.label_12.setText(_translate("MainWindow", "乘车终点："))
        self.pushButton_station.clicked.connect(self.getstation)

    def getstation(self):
        txt, ok = QInputDialog.getText(self, '输入框', '输入查询站点')
        if ok and txt:
            # self.lineEdit.setText(txt)
            # txt=str(txt)
            l = Station_inquiry(txt)
            self.lineEdit.setText(l)

