
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5 import QtWidgets

# ---------- We dont Touch --------------------
class Ui_Discovery(object):


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(682, 443)
        Form.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(140, 70, 441, 251))
        self.tableWidget.setStyleSheet("background-color: rgb(189, 193, 193);\n"
                                       "color: rgb(27, 28, 28);")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_submit = QtWidgets.QPushButton(Form)
        self.btn_submit.setGeometry(QtCore.QRect(270, 340, 181, 31))
        self.btn_submit.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(73, 199, 41);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 14pt \"Arial\";")
        self.btn_submit.setObjectName("btn_submit")
        self.l_title = QtWidgets.QLabel(Form)
        self.l_title.setGeometry(QtCore.QRect(220, 20, 251, 21))
        self.l_title.setStyleSheet("\n"
                                   "color:White;\n"
                                   "font: 18pt \".SF NS Text\";")
        self.l_title.setObjectName("l_title")
        self.btn_back = QtWidgets.QPushButton(Form)
        self.btn_back.setGeometry(QtCore.QRect(270, 390, 181, 31))
        self.btn_back.setStyleSheet("color: rgb(250, 255, 255);\n"
                                    "background-color: rgb(73, 199, 41);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "font: 14pt \"Arial\";")
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btn_submit.clicked.connect(self.load_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_submit.setText(_translate("Form", "Submit"))
        self.l_title.setText(_translate("Form", "Automated Host Discovery "))
        self.btn_back.setText(_translate("Form", "Back"))

class Ui_Outsecure(object):
    """
    LOGIN PAGE
    """
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

class Ui_NewUser(object):
    """
    NEW USERS
    """
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

# ----------------------------------------------


class Login(QtWidgets.QWidget,Ui_Outsecure):
    switch_window = QtCore.pyqtSignal()
    switch_window1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.btn_newuser.clicked.connect(self.btn_newuser_handler)
        self.btn_Submit.clicked.connect(self.btn_submit_handler)

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def bool_check_username(self):
        if len(self.txt_password.text()) <= 1:
            self.pop_message(text='Enter Valid Username and Password !')
        else:
            username = self.txt_username.text()
            password = self.txt_password.text()
            conn = sqlite3.connect('Data.db')
            cursor = conn.cursor()
            cursor.execute("SELECT username,password FROM credentials")
            val = cursor.fetchall()
            if len(val) >= 1:

                for x in val:
                    if username in x[0] and password in x[1]:
                        return True
                    else:
                        pass
            else:
                self.pop_message(text="No users Found ")
                return False

    def btn_submit_handler(self):
        val = self.bool_check_username()

        if (val):
            self.pop_message(text="Welcome ")
            self.switch_window1.emit()

        else:
            self.pop_message("Invalid username or password ")

    def btn_newuser_handler(self):
        self.switch_window.emit()

class Newuser(QtWidgets.QWidget, Ui_NewUser):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.Back.clicked.connect(self.back_handler)
        self.btn_submit.clicked.connect(self.btn_submit_handler)

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


    def btn_submit_handler(self):
        self.create_db_newuser()

    def back_handler(self):
        self.switch_window.emit()

    def create_db_newuser(self):

        txt_firstname_v = self.txt_firstname.text()
        txt_lastname_v = self.txt_lastname.text()
        txt_phone_v = self.txt_phone.text()
        txt_emailid_v = self.txt_email.text()
        txt_username_v =self.txt_username.text()
        txt_password_v =self.lineEdit.text()

        if (len(txt_firstname_v) <= 1
                and len(txt_lastname_v) <= 1 and
        len(txt_phone_v) <= 9  and
        len(txt_emailid_v) <= 1  and
        len(txt_username_v) <= 1  and
        len(txt_password_v) <=1):

            """
            Logic to see if users Enter all Feilds Correctly 
            """
            self.pop_message(text = "Please Enter All Feilds ")

        else:

            conn=sqlite3.connect('Data.db')
            cursor = conn.cursor()

            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS credentials 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    fname TEXT, 
                    lname TEXT, 
                    Phone TEXT, 
                    email TEXT,
                    username TEXT, 
                    password TEXT)""")

            cursor.execute(""" INSERT INTO credentials 
                    (fname,
                    lname,
                    Phone,
                    email,
                    username, 
                    password)
                    
                VALUES 
                (?,?,?,?,?,?)
                """,(txt_firstname_v, txt_lastname_v, txt_phone_v, txt_emailid_v,txt_username_v,txt_password_v))

            conn.commit()
            cursor.close()
            conn.close()
            self.pop_message(text="Added to Database ! ")


class Discovery(QtWidgets.QWidget, Ui_Discovery):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.btn_submit.clicked.connect(self.btn_submit_handler)
        self.btn_back.clicked.connect(self.btn_back_handler)

    def pop_message(self,text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def load_data(self):
        self.tableWidget.setItem(0,0, QtWidgets.QTableWidgetItem(str("Sr No")))
        self.tableWidget.setItem(0,1, QtWidgets.QTableWidgetItem(str(" Ip Address")))
        self.tableWidget.setItem(0,2, QtWidgets.QTableWidgetItem(str("Mac Address")))
        self.tableWidget.setItem(0,3, QtWidgets.QTableWidgetItem(str("Vendor")))

    def btn_submit_handler(self):
        self.load_data()

    def btn_back_handler(self):
        self.switch_window.emit()


class Controller:

    def __init__(self):
        pass

    def show_login_page(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_newuser_page)
        self.login.switch_window1.connect(self.show_discovery)
        self.login.show()

    def show_newuser_page(self):
        self.newuser = Newuser()
        self.newuser.switch_window.connect(self.show_login_page)
        self.login.close()
        self.newuser.show()

    def show_discovery(self):
        self.discovery = Discovery()
        self.discovery.switch_window.connect(self.show_login_page)
        self.login.close()
        self.discovery.show()



def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login_page()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()










