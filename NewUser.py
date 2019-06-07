# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewUser.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewUser(object):
    def setupUi(self, NewUser):
        NewUser.setObjectName("NewUser")
        NewUser.resize(555, 372)
        NewUser.setStyleSheet("background-color: rgb(14, 14, 14);")
        self.l_newuser = QtWidgets.QLabel(NewUser)
        self.l_newuser.setGeometry(QtCore.QRect(180, 10, 181, 31))
        self.l_newuser.setStyleSheet("font: 24pt \".SF NS Text\";\n"
                                     "color: rgb(234, 239, 238);\n"
                                     "")
        self.l_newuser.setAlignment(QtCore.Qt.AlignCenter)
        self.l_newuser.setObjectName("l_newuser")
        self.line = QtWidgets.QFrame(NewUser)
        self.line.setGeometry(QtCore.QRect(10, 50, 591, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txt_firstname = QtWidgets.QLineEdit(NewUser)
        self.txt_firstname.setEnabled(True)
        self.txt_firstname.setGeometry(QtCore.QRect(30, 80, 230, 41))
        self.txt_firstname.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                         "border-style:outset;\n"
                                         "border-radius:10px;\n"
                                         "font: 14pt \"Arial\";")
        self.txt_firstname.setText("")
        self.txt_firstname.setObjectName("txt_firstname")
        self.txt_lastname = QtWidgets.QLineEdit(NewUser)
        self.txt_lastname.setGeometry(QtCore.QRect(290, 80, 229, 41))
        self.txt_lastname.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_lastname.setObjectName("txt_lastname")
        self.txt_phone = QtWidgets.QLineEdit(NewUser)
        self.txt_phone.setGeometry(QtCore.QRect(30, 140, 230, 41))
        self.txt_phone.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                     "border-style:outset;\n"
                                     "border-radius:10px;\n"
                                     "font: 14pt \"Arial\";")
        self.txt_phone.setObjectName("txt_phone")
        self.txt_email = QtWidgets.QLineEdit(NewUser)
        self.txt_email.setGeometry(QtCore.QRect(290, 140, 229, 41))
        self.txt_email.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                     "border-style:outset;\n"
                                     "border-radius:10px;\n"
                                     "font: 14pt \"Arial\";")
        self.txt_email.setObjectName("txt_email")
        self.txt_username = QtWidgets.QLineEdit(NewUser)
        self.txt_username.setGeometry(QtCore.QRect(30, 200, 230, 41))
        self.txt_username.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                        "border-style:outset;\n"
                                        "border-radius:10px;\n"
                                        "font: 14pt \"Arial\";")
        self.txt_username.setObjectName("txt_username")
        self.lineEdit = QtWidgets.QLineEdit(NewUser)
        self.lineEdit.setGeometry(QtCore.QRect(290, 200, 231, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(207, 211, 211);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "font: 14pt \"Arial\";")
        self.lineEdit.setObjectName("lineEdit")
        self.btn_submit = QtWidgets.QPushButton(NewUser)
        self.btn_submit.setGeometry(QtCore.QRect(190, 270, 159, 31))
        self.btn_submit.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(73, 199, 41);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 14pt \"Arial\";")
        self.btn_submit.setObjectName("btn_submit")
        self.Back = QtWidgets.QPushButton(NewUser)
        self.Back.setGeometry(QtCore.QRect(190, 320, 159, 31))
        self.Back.setStyleSheet("color: rgb(250, 255, 255);\n"
                                "background-color: rgb(73, 199, 41);\n"
                                "border-style:outset;\n"
                                "border-radius:10px;\n"
                                "font: 14pt \"Arial\";")
        self.Back.setObjectName("Back")

        self.retranslateUi(NewUser)
        QtCore.QMetaObject.connectSlotsByName(NewUser)

    def retranslateUi(self, NewUser):
        _translate = QtCore.QCoreApplication.translate
        NewUser.setWindowTitle(_translate("NewUser", "Form"))
        self.l_newuser.setText(_translate("NewUser", "New User"))
        self.txt_firstname.setPlaceholderText(_translate("NewUser", "Enter your First Name"))
        self.txt_lastname.setPlaceholderText(_translate("NewUser", "Enter your Last Name"))
        self.txt_phone.setPlaceholderText(_translate("NewUser", "Enter your Phone Number "))
        self.txt_email.setPlaceholderText(_translate("NewUser", "Enter your Email Address "))
        self.txt_username.setPlaceholderText(_translate("NewUser", "Enter Username"))
        self.lineEdit.setPlaceholderText(_translate("NewUser", "Enter Password"))
        self.btn_submit.setText(_translate("NewUser", "Submit"))
        self.Back.setText(_translate("NewUser", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewUser = QtWidgets.QWidget()
    ui = Ui_NewUser()
    ui.setupUi(NewUser)
    NewUser.show()
    sys.exit(app.exec_())

