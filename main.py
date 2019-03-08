from PyQt5 import QtCore, QtGui, QtWidgets
from docx import Document #pip install python-docx
import mysql.connector
import pymsgbox
import time

cnx = mysql.connector.connect(user='root', password='i130813',
                              host='134.0.113.52',
                              database='aero')
cursor = cnx.cursor()

user_id = 0


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.workerlabel = QtWidgets.QLabel(self.centralwidget)
        self.workerlabel.setObjectName("workerlabel")
        self.gridLayout.addWidget(self.workerlabel, 0, 0, 1, 1)
        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.setObjectName("exitbutton")
        self.gridLayout.addWidget(self.exitbutton, 0, 2, 1, 1)
        self.accountbuton = QtWidgets.QPushButton(self.centralwidget)
        self.accountbuton.setObjectName("accountbuton")
        self.gridLayout.addWidget(self.accountbuton, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.workerlabel.setText(_translate("MainWindow", "Вы авторизованы как:"))
        self.exitbutton.setText(_translate("MainWindow", "Выход"))
        self.accountbuton.setText(_translate("MainWindow", "Личная карточка"))

        global user_id
        query = "select fio from part_team where worker_id = %s"
        data = (user_id,)
        cursor.execute(query, data)
        for item in cursor:
            for value in item:
                self.workerlabel.setText("Вы авторизованы как: " + str(value))

    def setupLoginUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(442, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.loginedit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginedit.sizePolicy().hasHeightForWidth())
        self.loginedit.setSizePolicy(sizePolicy)
        self.loginedit.setObjectName("loginedit")
        self.gridLayout.addWidget(self.loginedit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.passedit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passedit.sizePolicy().hasHeightForWidth())
        self.passedit.setSizePolicy(sizePolicy)
        self.passedit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.passedit.setAlignment(QtCore.Qt.AlignCenter)
        self.passedit.setObjectName("passedit")
        self.gridLayout.addWidget(self.passedit, 2, 1, 1, 1)
        self.loginbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginbutton.sizePolicy().hasHeightForWidth())
        self.loginbutton.setSizePolicy(sizePolicy)
        self.loginbutton.setObjectName("loginbutton")
        self.gridLayout.addWidget(self.loginbutton, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 442, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateLoginUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateLoginUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Логин"))
        self.label.setText(_translate("MainWindow", "Вход в систему"))
        self.label_3.setText(_translate("MainWindow", "Пароль"))
        self.loginbutton.setText(_translate("MainWindow", "Вход"))

        self.loginbutton.clicked.connect(self.login)

    def login(self):
        try:
            query = "select pass from worker where worker_id = %s"
            data = (self.loginedit.text(),)
            cursor.execute(query, data)
            for item in cursor:
                for value in item:
                    if str(value) == self.passedit.text():
                        global user_id
                        user_id = self.loginedit.text()
                        self.setupUi()
        except BaseException:
            pymsgbox.alert("Проверьте правильность данных", "Ошибка")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupLoginUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

