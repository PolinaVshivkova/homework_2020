# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 415)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 481, 361))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(510, 210, 90, 160))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_update = QtWidgets.QPushButton(self.widget1)
        self.pushButton_update.setObjectName("pushButton_create")
        self.verticalLayout.addWidget(self.pushButton_update)
        self.pushButton_recently = QtWidgets.QPushButton(self.widget1)
        self.pushButton_recently.setObjectName("pushButton_create")
        self.verticalLayout.addWidget(self.pushButton_recently)
        self.pushButton_reading = QtWidgets.QPushButton(self.widget1)
        self.pushButton_reading.setObjectName("pushButton_reading")
        self.verticalLayout.addWidget(self.pushButton_reading)
        self.pushButton_create = QtWidgets.QPushButton(self.widget1)
        self.pushButton_create.setObjectName("pushButton_create")
        self.verticalLayout.addWidget(self.pushButton_create)
        self.pushButton_delite = QtWidgets.QPushButton(self.widget1)
        self.pushButton_delite.setObjectName("pushButton_delite")
        self.verticalLayout.addWidget(self.pushButton_delite)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моя библиотека"))
        self.label.setText(_translate("MainWindow", "Список книг:"))
        self.pushButton_reading.setText(_translate("MainWindow", "Непрочитанные"))
        self.pushButton_create.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_delite.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_recently.setText(_translate("MainWindow", "Прочитано"))
        self.pushButton_update.setText(_translate("MainWindow", "Обновить"))
