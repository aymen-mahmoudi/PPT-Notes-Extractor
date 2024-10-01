# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(596, 219)
        Form.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(212, 54, 197, 29), stop:0.218905 rgba(251, 102, 0, 145), stop:0.375 rgba(255, 255, 0, 69), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(9, 10, 571, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.path_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.path_lineEdit.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.path_lineEdit.setObjectName("path_lineEdit")
        self.gridLayout.addWidget(self.path_lineEdit, 0, 1, 1, 1)
        self.browse_pushButton = QtWidgets.QPushButton(self.frame)
        self.browse_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browse_pushButton.setStyleSheet("background-color: rgb(255, 247, 20);\n"
"font: 75 10pt \"Cascadia Mono\";\n"
"")
        self.browse_pushButton.setObjectName("browse_pushButton")
        self.gridLayout.addWidget(self.browse_pushButton, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delete_pushButton = QtWidgets.QPushButton(self.frame)
        self.delete_pushButton.setStyleSheet("background-color: rgb(255, 19, 19);\n"
"font: 75 10pt \"Cascadia Mono\";")
        self.delete_pushButton.setObjectName("delete_pushButton")
        self.horizontalLayout.addWidget(self.delete_pushButton)
        self.export_pushButton = QtWidgets.QPushButton(self.frame)
        self.export_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.export_pushButton.setStyleSheet("background-color: rgb(185, 255, 211);\n"
"font: 75 10pt \"Cascadia Mono\";")
        self.export_pushButton.setObjectName("export_pushButton")
        self.horizontalLayout.addWidget(self.export_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PPTX Notes Extractor (by aymen mahmoudi) V 1.0"))
        self.label.setText(_translate("Form", "PPT notes Extractor"))
        self.browse_pushButton.setText(_translate("Form", "Browse"))
        self.delete_pushButton.setText(_translate("Form", "Delete"))
        self.export_pushButton.setText(_translate("Form", "Export"))
