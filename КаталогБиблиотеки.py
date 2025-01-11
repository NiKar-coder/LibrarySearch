import sys
import sqlite3

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPixmap

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 90, 191, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(280, 30, 151, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.table.setGeometry(QtCore.QRect(0, 140, 501, 361))
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Каталог библиотеки"))
        self.btn.setText(_translate("MainWindow", "Искать"))


class Biblio(QMainWindow, Ui_1):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.retranslateUi(self)

        self.comboBox.addItem('Название')
        self.comboBox.addItem('Автор')
        self.btn.clicked.connect(self.searches)

        db = sqlite3.connect('database.sqlite')

        cur = db.cursor()

        self.data = cur.execute("""SELECT Books.title,
        Authors.name, Books.year, Genres.name, Books.picture FROM Books
                    JOIN Authors ON Books.author_id = Authors.id
                    JOIN Genres ON Books.genre_id = Genres.id""").fetchall()

        db.close()

    def searches(self):
        if self.comboBox.currentText() == 'Название':
            books = [i for i in self.data if self.lineEdit.text().lower()
                     in i[0].lower()]
        else:
            books = [i for i in self.data if self.lineEdit.text().lower()
                     in i[1].lower()]

        self.table.setColumnCount(1)
        self.table.setRowCount(len(books))

        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)

        self.table.setColumnWidth(0, 500)

        for i in range(len(books)):
            btn = QPushButton(books[i][0])
            btn.clicked.connect(lambda checked: self.book_info())

            self.table.setCellWidget(i, 0, btn)

    def book_info(self):
        el = [i for i in self.data if i[0] == self.sender().text()]

        self.widget = Book(el[0][0], el[0][1], el[0][2], el[0][3], el[0][4])
        self.widget.show()


class Ui_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 0, 100, 100))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 110, 301, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 130, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setText("")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter |
            QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_4.setObjectName("label_4")
        self.author = QtWidgets.QLabel(parent=self.centralwidget)
        self.author.setGeometry(QtCore.QRect(30, 200, 221, 31))
        self.author.setText("")
        self.author.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.author.setObjectName("author")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 245, 211, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.year = QtWidgets.QLabel(parent=self.centralwidget)
        self.year.setGeometry(QtCore.QRect(30, 270, 221, 21))
        self.year.setText("")
        self.year.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.year.setObjectName("year")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 290, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.genre = QtWidgets.QLabel(parent=self.centralwidget)
        self.genre.setGeometry(QtCore.QRect(50, 330, 191, 31))
        self.genre.setText("")
        self.genre.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.genre.setObjectName("genre")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Информация о произведении"))
        self.label_2.setText(_translate("MainWindow", "Название"))
        self.label_4.setText(_translate("MainWindow", "Автор"))
        self.label_6.setText(_translate("MainWindow", "Год выпуска"))
        self.label_8.setText(_translate("MainWindow", "Жанр"))


class Book(QMainWindow, Ui_2):
    def __init__(self, title, author, year, genre, picture):
        super().__init__()

        self.setupUi(self)
        self.retranslateUi(self)

        self.title.setText(title)
        self.author.setText(author)
        self.year.setText(year)
        self.genre.setText(genre)

        self.pixmap = QPixmap(picture)

        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Biblio()
    ex.show()
    sys.exit(app.exec())
