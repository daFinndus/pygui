# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pygui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PyGUI(object):
    def setupUi(self, PyGUI):
        PyGUI.setObjectName("PyGUI")
        PyGUI.resize(692, 528)
        self.centralwidget = QtWidgets.QWidget(PyGUI)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(110, 130, 461, 61))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.temperature_ouput = QtWidgets.QLineEdit(self.groupBox)
        self.temperature_ouput.setGeometry(QtCore.QRect(290, 30, 151, 20))
        self.temperature_ouput.setText("")
        self.temperature_ouput.setReadOnly(True)
        self.temperature_ouput.setClearButtonEnabled(False)
        self.temperature_ouput.setObjectName("temperature_ouput")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 271, 16))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(110, 210, 461, 131))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBox_temp_unit = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_temp_unit.setGeometry(QtCore.QRect(290, 80, 151, 22))
        self.comboBox_temp_unit.setObjectName("comboBox_temp_unit")
        self.comboBox_temp_unit.addItem("")
        self.comboBox_temp_unit.addItem("")
        self.comboBox_temp_unit.addItem("")
        self.sampling_time_input = QtWidgets.QLineEdit(self.groupBox_2)
        self.sampling_time_input.setGeometry(QtCore.QRect(290, 40, 151, 20))
        self.sampling_time_input.setObjectName("sampling_time_input")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 271, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 271, 16))
        self.label_3.setObjectName("label_3")
        self.sampling_time_input.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.comboBox_temp_unit.raise_()
        self.button_update = QtWidgets.QPushButton(self.centralwidget)
        self.button_update.setGeometry(QtCore.QRect(110, 350, 111, 23))
        self.button_update.setObjectName("button_update")
        self.button_start = QtWidgets.QPushButton(self.centralwidget)
        self.button_start.setGeometry(QtCore.QRect(280, 350, 111, 23))
        self.button_start.setObjectName("button_start")
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(460, 350, 111, 23))
        self.button_stop.setObjectName("button_stop")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.button_update.raise_()
        self.button_start.raise_()
        self.button_stop.raise_()
        PyGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 692, 21))
        self.menubar.setObjectName("menubar")
        self.menuApplication_by_Darren_Jonas_and_Finn = QtWidgets.QMenu(self.menubar)
        self.menuApplication_by_Darren_Jonas_and_Finn.setSeparatorsCollapsible(False)
        self.menuApplication_by_Darren_Jonas_and_Finn.setObjectName("menuApplication_by_Darren_Jonas_and_Finn")
        PyGUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyGUI)
        self.statusbar.setObjectName("statusbar")
        PyGUI.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuApplication_by_Darren_Jonas_and_Finn.menuAction())

        self.retranslateUi(PyGUI)
        QtCore.QMetaObject.connectSlotsByName(PyGUI)

    def retranslateUi(self, PyGUI):
        _translate = QtCore.QCoreApplication.translate
        PyGUI.setWindowTitle(_translate("PyGUI", "MainWindow"))
        self.groupBox.setTitle(_translate("PyGUI", "Input data"))
        self.label.setText(_translate("PyGUI", "Current temperature"))
        self.groupBox_2.setTitle(_translate("PyGUI", "Parameterization"))
        self.comboBox_temp_unit.setItemText(0, _translate("PyGUI", "Kelvin [ K ]"))
        self.comboBox_temp_unit.setItemText(1, _translate("PyGUI", "Celsius [ °C ]"))
        self.comboBox_temp_unit.setItemText(2, _translate("PyGUI", "Fahrenheit [ °F ]"))
        self.label_2.setText(_translate("PyGUI", "Sampling time in ms"))
        self.label_3.setText(_translate("PyGUI", "Unit of temperature"))
        self.button_update.setText(_translate("PyGUI", "Update"))
        self.button_start.setText(_translate("PyGUI", "Start"))
        self.button_stop.setText(_translate("PyGUI", "Stop"))
        self.menuApplication_by_Darren_Jonas_and_Finn.setTitle(_translate("PyGUI", "Temperature Application"))