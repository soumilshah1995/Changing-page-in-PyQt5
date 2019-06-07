# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Outsecure(object):
    def setupUi(self, Outsecure):
        Outsecure.setObjectName("Outsecure")
        Outsecure.resize(529, 342)
        Outsecure.setMouseTracking(True)
        Outsecure.setStyleSheet("background-color: rgb(8, 8, 8);")
        self.line = QtWidgets.QFrame(Outsecure)
        self.line.setGeometry(QtCore.QRect(10, 80, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.l_title = QtWidgets.QLabel(Outsecure)
        self.l_title.setGeometry(QtCore.QRect(170, 20, 231, 41))
        self.l_title.setStyleSheet("color: rgb(242, 247, 247);\n"
                                   "font: 30pt \".SF NS Text\";")
        self.l_title.setObjectName("l_title")
        self.btn_Submit = QtWidgets.QPushButton(Outsecure)
        self.btn_Submit.setGeometry(QtCore.QRect(180, 200, 161, 31))
        self.btn_Submit.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(73, 199, 41);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 14pt \"Arial\";")
        self.btn_Submit.setObjectName("btn_Submit")
        self.btn_newuser = QtWidgets.QPushButton(Outsecure)
        self.btn_newuser.setGeometry(QtCore.QRect(180, 240, 161, 31))
        self.btn_newuser.setStyleSheet("color: rgb(250, 255, 255);\n"
                                       "background-color: rgb(73, 199, 41);\n"
                                       "border-style:outset;\n"
                                       "border-radius:10px;\n"
                                       "font: 14pt \"Arial\";")
        self.btn_newuser.setObjectName("btn_newuser")
        self.l_copyright = QtWidgets.QLabel(Outsecure)
        self.l_copyright.setGeometry(QtCore.QRect(150, 310, 261, 21))
        self.l_copyright.setStyleSheet("color: rgb(252, 0, 28);")
        self.l_copyright.setObjectName("l_copyright")
        self.txt_username = QtWidgets.QLineEdit(Outsecure)
        self.txt_username.setGeometry(QtCore.QRect(130, 100, 275, 31))
        self.txt_username.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_username.setObjectName("txt_username")
        self.txt_password = QtWidgets.QLineEdit(Outsecure)
        self.txt_password.setGeometry(QtCore.QRect(130, 150, 271, 31))
        self.txt_password.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_password.setObjectName("txt_password")

        self.retranslateUi(Outsecure)
        QtCore.QMetaObject.connectSlotsByName(Outsecure)

    def retranslateUi(self, Outsecure):
        _translate = QtCore.QCoreApplication.translate
        Outsecure.setWindowTitle(_translate("Outsecure", "Form"))
        self.l_title.setText(_translate("Outsecure", "Login Page"))
        self.btn_Submit.setText(_translate("Outsecure", "Submit"))
        self.btn_newuser.setText(_translate("Outsecure", "New User"))
        self.l_copyright.setText(_translate("Outsecure", "This software belongs to OutSecure "))
        self.txt_username.setPlaceholderText(_translate("Outsecure", "Enter UserName"))
        self.txt_password.setPlaceholderText(_translate("Outsecure", "Enter Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Outsecure = QtWidgets.QWidget()
    ui = Ui_Outsecure()
    ui.setupUi(Outsecure)
    Outsecure.show()
    sys.exit(app.exec_())

