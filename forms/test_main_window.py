# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TestWindow(object):
    def setupUi(self, TestWindow):
        TestWindow.setObjectName("TestWindow")
        TestWindow.resize(800, 400)
        TestWindow.setMinimumSize(QtCore.QSize(800, 400))
        TestWindow.setMaximumSize(QtCore.QSize(800, 400))
        self.centralwidget = QtWidgets.QWidget(TestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(569, 20, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 311, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 170, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 120, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 190, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 260, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(566, 333, 201, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 240, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 240, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        TestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TestWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        TestWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TestWindow)
        self.statusbar.setObjectName("statusbar")
        TestWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(TestWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(TestWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(TestWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(TestWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(TestWindow)
        QtCore.QMetaObject.connectSlotsByName(TestWindow)

    def retranslateUi(self, TestWindow):
        _translate = QtCore.QCoreApplication.translate
        TestWindow.setWindowTitle(_translate("TestWindow", "Budget"))
        self.lineEdit.setText(_translate("TestWindow", "123"))
        self.label.setText(_translate("TestWindow", "Поступления:"))
        self.label_2.setText(_translate("TestWindow", "Траты"))
        self.lineEdit_2.setText(_translate("TestWindow", "321"))
        self.pushButton.setText(_translate("TestWindow", "День"))
        self.pushButton_2.setText(_translate("TestWindow", "Неделя"))
        self.pushButton_3.setText(_translate("TestWindow", "Месяц"))
        self.label_3.setText(_translate("TestWindow", "powered by svetgrak"))
        self.pushButton_4.setText(_translate("TestWindow", "Добавить деняг"))
        self.pushButton_5.setText(_translate("TestWindow", "Тратить!"))
        self.menu.setTitle(_translate("TestWindow", "База"))
        self.action.setText(_translate("TestWindow", "Создать базу"))
        self.action_2.setText(_translate("TestWindow", "Удалить базу"))
        self.action_3.setText(_translate("TestWindow", "Создать таблицу"))
        self.action_4.setText(_translate("TestWindow", "Заполнить таблицу тестовыми данными"))
