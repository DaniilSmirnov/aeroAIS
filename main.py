from PyQt5 import QtCore, QtGui, QtWidgets
from docx import Document #pip install python-docx
import mysql.connector
import pymsgbox
import time

try:
    cnx = mysql.connector.connect(user='root', password='i130813',
                                  host='134.0.113.52',
                                  database='aero')
    cursor = cnx.cursor(buffered=True)
except Exception as e:
    pymsgbox.alert("Произошла ошибка \n" + str(e), "Ошибка")

user_id = 0

workers_edit = {}
workers_data = {}


class Ui_MainWindow(object):
    def setupUi(self):
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

        self.accountbuton.clicked.connect(self.setupAccUi)
        self.exitbutton.clicked.connect(self.setupUi)

        global user_id
        query = "select fio from part_team where workerid = %s"
        data = (user_id,)
        cursor.execute(query, data)
        for item in cursor:
            for value in item:
                self.workerlabel.setText("Вы авторизованы как: " + str(value))

    def setupLoginUi(self):
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
            query = "select password from part_team where workerid = %s"
            data = (self.loginedit.text(),)
            cursor.execute(query, data)
            for item in cursor:
                for value in item:
                    if str(value) == self.passedit.text():
                        global user_id
                        user_id = self.loginedit.text()
                        query = "select position from part_team where workerid = %s"
                        cursor.execute(query, data)
                        for item in cursor:
                            for value in item:
                                if str(value) != "Админ":
                                    self.setupUi()
                                else:
                                    self.setupAdminUi()
        except BaseException:
            pymsgbox.alert("Проверьте правильность данных", "Ошибка")

    def setupAccUi(self):
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
        self.modifybutton = QtWidgets.QPushButton(self.centralwidget)
        self.modifybutton.setObjectName("modifybutton")
        self.gridLayout.addWidget(self.modifybutton, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateAccUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateAccUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.workerlabel.setText(_translate("MainWindow", "Вы авторизованы как:"))
        self.exitbutton.setText(_translate("MainWindow", "Назад"))
        self.modifybutton.setText(_translate("MainWindow", "Применить изменения"))

        self.exitbutton.clicked.connect(self.setupUi)
        self.modifybutton.hide()

        global user_id
        query = "select fio from part_team where workerid = %s"
        data = (user_id,)
        cursor.execute(query, data)
        for item in cursor:
            for value in item:
                self.workerlabel.setText("Вы авторизованы как: " + str(value))

        query = "select * from part_team where workerid = %s"
        cursor.execute(query, data)

        i = 1
        for item in cursor:
            for value in item:
                if str(value) == "None":
                    continue
                else:
                    if i == 1:
                        value = "Ваш Логин: " + str(value)
                    if i == 2:
                        value = "Вас зовут: " + str(value)
                    if i == 3:
                        value = "Ваш стаж: " + str(value)
                    if i == 4:
                        value = "Уровень образования: " + str(value)
                    if i == 5:
                        value = "Паспорт: " + str(value)
                    if i == 6:
                        value = "Статус: " + str(value)
                    if i == 7:
                        value = "Дата начала работы: " + str(value)
                    if i == 8:
                        value = "Место работы: " + str(value)
                    if i == 9:
                        value = "Должность: " + str(value)
                    if i == 10:
                        value = "Для смены данных или пароля обратитесь к администратору"
                    item_label = QtWidgets.QLabel(value)
                    self.gridLayout.addWidget(item_label, i, 0, 1, 1)
                    i += 1

    def setupAdminUi(self):
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
        self.gridLayout.addWidget(self.exitbutton, 0, 3, 1, 1)
        self.modifybutton = QtWidgets.QPushButton(self.centralwidget)
        self.modifybutton.setObjectName("modifybutton")
        self.gridLayout.addWidget(self.modifybutton, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 490, 322))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateAdminUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateAdminUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.workerlabel.setText(_translate("MainWindow", "Вы авторизованы как:"))
        self.exitbutton.setText(_translate("MainWindow", "Назад"))
        self.modifybutton.setText(_translate("MainWindow", "Применить изменения"))
        self.pushButton.setText(_translate("MainWindow", "Добавить сотрудника"))

        self.exitbutton.clicked.connect(self.setupLoginUi)
        self.pushButton.clicked.connect(self.setupAddWorkerUi)

        global user_id
        query = "select fio from part_team where workerid = %s"
        data = (user_id,)
        cursor.execute(query, data)
        for item in cursor:
            for value in item:
                self.workerlabel.setText("Вы авторизованы как: " + str(value))

        query = "select * from part_team"
        cursor.execute(query)

        label_item = QtWidgets.QLabel("Работники")
        self.gridLayout_2.addWidget(label_item, 0, 0, 1, 1)

        i = 0
        labels = ["Логин (ID)", "ФИО", "Cтаж", "Уровень образования", "Паспорт", "Cтатус", "Дата найма", "Дата увольнения", "Компания", "Пароль", "Должность"]
        for label in labels:
            label_item = QtWidgets.QLabel(label)
            self.gridLayout_2.addWidget(label_item, 1, i, 1, 1)
            i += 1

        i = 2
        j = 0
        for item in cursor:
            for value in item:
                if j == 0 or j == 6 or j == 7:
                    if j == 0:
                        buf = str(value)
                    label_item = QtWidgets.QLabel(str(value))
                    self.gridLayout_2.addWidget(label_item, i, j, 1, 1)
                else:
                    edit_item = QtWidgets.QLineEdit(str(value))
                    self.gridLayout_2.addWidget(edit_item, i, j, 1, 1)
                    edit_item.textChanged.connect(lambda state, line=[edit_item, edit_item.text(), j]: modify_worker(line))
                j += 1

            button_item = QtWidgets.QPushButton("Уволить")
            button_item.clicked.connect(lambda state, id=buf: fire_worker(id))
            self.gridLayout_2.addWidget(button_item, i, j+1, 1, 1)

            i += 1
            j = 0

        query = "select * from team"
        cursor.execute(query)

        j = 0
        label_item = QtWidgets.QLabel("Экипажи")
        self.gridLayout_2.addWidget(label_item, i, j, 1, 1)

        labels = ["Номер Экипажа", "Номер рейса", "Дата медосмотра", "Причина", "Допуск", "ID работника"]
        for label in labels:
            label_item = QtWidgets.QLabel(label)
            self.gridLayout_2.addWidget(label_item, i+1, j, 1, 1)
            j += 1
        i += 2
        j = 0

        for item in cursor:
            for value in item:
                if j == 0:
                    if j == 0:
                        buf = str(value)
                    label_item = QtWidgets.QLabel(str(value))
                    self.gridLayout_2.addWidget(label_item, i, j, 1, 1)
                else:
                    edit_item = QtWidgets.QLineEdit(str(value))
                    self.gridLayout_2.addWidget(edit_item, i, j, 1, 1)
                j += 1

            button_item = QtWidgets.QPushButton("Удалить")
            button_item.clicked.connect(lambda state, id=buf: delete_team(id))
            self.gridLayout_2.addWidget(button_item, i, j + 1, 1, 1)

            i += 1
            j = 0

        def fire_worker(id):
            try:
                query = "update part_team set stat = 'Уволен' where workerid = %s;"
                data = (id, )
                cursor.execute(query, data)
                query = "update part_team set f_date = NOW() where workerid = %s;"
                cursor.execute(query, data)
            except mysql.connector.errors.InternalError:
                pass
            cnx.commit()
            pymsgbox.alert("Сотрудник уволен", "Инфо")
            self.setupAdminUi()

        def delete_team(id):
            query = "delete from team where idteam = %s"
            data = (id, )
            cursor.execute(query, data)
            cnx.commit()
            pymsgbox.alert("Экипаж удален", "Инфо")
            self.setupAdminUi()

        def modify_worker(item):
            self.modifybutton.clicked.connect(lambda: save_worker(item))

        def save_worker(item):
            index = int(item[2])
            data = (item[0].text(), item[1])
            if index == 1:
                query = "update part_team set fio = %s where fio = %s;"
            if index == 2:
                query = "update part_team set work_time = %s where work_time = %s;"
            if index == 3:
                query = "update part_team set edu = %s where edu = %s;"
            if index == 4:
                query = "update part_team set pass = %s where pass = %s;"
            if index == 5:
                query = "update part_team set stat = %s where stat = %s;"
            if index == 8:
                query = "update part_team set cname = %s where cname = %s;"
            if index == 9:
                query = "update part_team set password = %s where password = %s;"
            if index == 10:
                query = "update part_team set position = %s where position = %s;"
            cursor.execute(query, data)
            cnx.commit()

    def setupAddWorkerUi(self):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 412)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 1, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 3)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 1, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 5, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 7, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 1, 7, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 1, 6, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateAddWorkerUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateAddWorkerUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Подтвердить"))
        self.pushButton_2.setText(_translate("MainWindow", "Отменить"))
        self.label_2.setText(_translate("MainWindow", "Должность"))
        self.label_4.setText(_translate("MainWindow", "Паспорт"))
        self.label_3.setText(_translate("MainWindow", "Уровень образования"))
        self.label_8.setText(_translate("MainWindow", "Компания"))
        self.label_9.setText(_translate("MainWindow", "Пароль"))
        self.label_5.setText(_translate("MainWindow", "Статус"))
        self.label.setText(_translate("MainWindow", "ФИО"))

        self.pushButton.clicked.connect(self.add_worker)

    def add_worker(self):
        query = "insert into part_team values (default, %s, '0', %s, %s, %s, NOW(), null, %s, %s, %s)"
        data = (self.lineEdit.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(),
                self.lineEdit_8.text(), self.lineEdit_9.text(), self.lineEdit_2.text())
        cursor.execute(query, data)
        cnx.commit()
        pymsgbox.alert("Пользователь добавлен", "Инфо")
        self.setupAdminUi()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupAdminUi()
    MainWindow.show()
    sys.exit(app.exec_())

