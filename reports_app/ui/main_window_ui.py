# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.report_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.report_pushButton.setGeometry(QtCore.QRect(568, 510, 171, 31))
        self.report_pushButton.setObjectName("report_pushButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 281, 181))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(0, 20, 281, 141))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.object_name_lineEdit = QtWidgets.QLineEdit(self.widget)
        self.object_name_lineEdit.setObjectName("object_name_lineEdit")
        self.gridLayout.addWidget(self.object_name_lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.report_name_spinBox = QtWidgets.QSpinBox(self.widget)
        self.report_name_spinBox.setObjectName("report_name_spinBox")
        self.gridLayout.addWidget(self.report_name_spinBox, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.report_dat_dateEdit = QtWidgets.QDateEdit(self.widget)
        self.report_dat_dateEdit.setObjectName("report_dat_dateEdit")
        self.gridLayout.addWidget(self.report_dat_dateEdit, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.measure_start_timeEdit = QtWidgets.QTimeEdit(self.widget)
        self.measure_start_timeEdit.setObjectName("measure_start_timeEdit")
        self.gridLayout.addWidget(self.measure_start_timeEdit, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.measure_end_timeEdit = QtWidgets.QTimeEdit(self.widget)
        self.measure_end_timeEdit.setObjectName("measure_end_timeEdit")
        self.gridLayout.addWidget(self.measure_end_timeEdit, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menutest = QtWidgets.QMenu(self.menubar)
        self.menutest.setObjectName("menutest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menutest.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.report_pushButton.setText(_translate("MainWindow", "Сгенерировать отчет"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "Название объекта"))
        self.label_2.setText(_translate("MainWindow", "Номер отчета"))
        self.label_3.setText(_translate("MainWindow", "Дата"))
        self.label_4.setText(_translate("MainWindow", "Время (начало)"))
        self.label_5.setText(_translate("MainWindow", "Время (конец)"))
        self.menutest.setTitle(_translate("MainWindow", "test"))
