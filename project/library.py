import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QErrorMessage
from project.main import Ui_MainWindow
from project.form import Ui_Form
from project.Reading import Ui_Reading


class ListOfBooks(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update()
        self.pushButton_create.clicked.connect(self.create_new)
        self.pushButton_reading.clicked.connect(self.reading)
        self.pushButton_delite.clicked.connect(self.delete)
        self.pushButton_recently.clicked.connect(self.recently)
        self.pushButton_update.clicked.connect(self.update)
        self.titles = None
        self.tableWidget.setHorizontalHeaderLabels(["Название книги", "Автор", "Жанр", ""])
        self.tableWidget.resizeColumnsToContents()
        self.con.close()

    def update(self):
        self.con = sqlite3.connect("bd.library.db")
        cur = self.con.cursor()

        result = cur.execute("SELECT name, author, genres, flag FROM books ").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}

    def recently(self):
        self.con = sqlite3.connect("bd.library.db")
        cur = self.con.cursor()
        index = self.tableWidget.selectionModel().selectedRows()
        if len(index) == 1:
            elem = self.tableWidget.item(index[0].row(), 0).text()
            print(f'''UPDATE books SET flag="T" WHERE name = {elem}''')
            cur.execute(f'''UPDATE books SET flag="T" WHERE name = "{elem}"''')
        self.con.commit()
        self.con.close()

    def create_new(self):
        ex1 = Form()
        ex1.exec_()
        self.tableWidget.updatesEnabled()

    def reading(self):
        ex2 = Reading()
        ex2.exec_()

    def delete(self):
        self.con = sqlite3.connect("bd.library.db")
        cur = self.con.cursor()
        index = self.tableWidget.selectionModel().selectedRows()
        if len(index) == 1:
            elem = self.tableWidget.item(index[0].row(), 0).text()
            print(f'''DELETE FROM books WHERE name = {elem}''')
            cur.execute(f'''DELETE FROM books WHERE name = "{elem}"''')
            self.tableWidget.removeRow(index[0].row())

        self.con.commit()
        self.con.close()


class Form(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_new.clicked.connect(self.create_new)
        self.con = sqlite3.connect("bd.library.db")

    def create_new(self):
        cur = self.con.cursor()
        row = cur.execute("""SELECT name FROM books""").fetchall()
        if self.checkBox.isChecked():
            flag = "T"
        else:
            flag = "F"
        if self.lineEdit.text() and self.lineEdit_2.text() and self.lineEdit_3.text():
            data = (len(row) + 1, self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), flag)
            cur.execute("INSERT INTO books VALUES(?, ?, ?, ?, ?) ", data).fetchall()
        else:
            self.close_dialog()
            error_dialog = QErrorMessage()
            error_dialog.showMessage("Введены не все данные")
            error_dialog.exec_()
        self.con.commit()
        self.con.close()
        self.close_dialog()

    def close_dialog(self):
        self.close()


class Reading(QDialog, Ui_Reading):
    def __init__(self):
        super().__init__()
        self.setupUi2(self)
        self.con = sqlite3.connect("bd.library.db")
        cur = self.con.cursor()

        result1 = cur.execute("SELECT name, author, genres, flag FROM books WHERE flag='F'").fetchall()
        self.tableWidget.setRowCount(len(result1))
        self.tableWidget.setColumnCount(len(result1[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result1):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}
        self.titles = None
        self.tableWidget.setHorizontalHeaderLabels(["Название книги", "Автор", "Жанр", ""])
        self.tableWidget.resizeColumnsToContents()
        self.con.close()


app = QApplication(sys.argv)
ex = ListOfBooks()
ex.show()
sys.exit(app.exec_())