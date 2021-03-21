# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'realweather.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RealTime(object):
    def setupUi(self, RealTime):
        RealTime.setObjectName("RealTime")
        RealTime.resize(473, 288)
        self.horizontalLayoutWidget = QtWidgets.QWidget(RealTime)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 181, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label1.setObjectName("label1")
        self.horizontalLayout.addWidget(self.label1)
        self.weathernumber = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.weathernumber.setObjectName("weathernumber")
        self.horizontalLayout.addWidget(self.weathernumber)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(RealTime)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(9, 138, 181, 101))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.weatherwhat = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.weatherwhat.setObjectName("weatherwhat")
        self.horizontalLayout_2.addWidget(self.weatherwhat)
        self.label_pix = QtWidgets.QLabel(RealTime)
        self.label_pix.setGeometry(QtCore.QRect(240, 76, 121, 81))
        self.label_pix.setObjectName("label_pix")

        self.retranslateUi(RealTime)
        QtCore.QMetaObject.connectSlotsByName(RealTime)

    def retranslateUi(self, RealTime):
        _translate = QtCore.QCoreApplication.translate
        RealTime.setWindowTitle(_translate("RealTime", "Form"))
        self.label1.setText(_translate("RealTime", "温度："))
        self.weathernumber.setText(_translate("RealTime", "1"))
        self.label_2.setText(_translate("RealTime", "天气"))
        self.weatherwhat.setText(_translate("RealTime", "晴空万里"))
        self.label_pix.setText(_translate("RealTime", "pix"))
