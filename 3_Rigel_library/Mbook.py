# _*_ coding: utf-8 _*_


from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QComboBox, QMessageBox, QMenu, QAction, QHeaderView, QAbstractItemView
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot, QSize, Qt
from PyQt5.QtWidgets import QApplication

from Library_mainUI import Ui_L_MainUi
from datamanage import DataMana
from createbook import CreateBook

import sys

class MainBook(QMainWindow, Ui_L_MainUi):
    bookdb = DataMana()
    booklist = []
    def __init__(self, parent=None):
        super(MainBook, self).__init__(parent)
        self.setupUi(self)
        self.showtable()


    def showtable(self):
        self.booklist = self.bookdb.loadbook()
        list_rows = len(self.booklist)
        table_rows = self.tableWidget.rowCount()

        if table_rows == 0 and list_rows > 0:
             self.selectTable(self.booklist)

    def selectTable(self, booklist):
        for i, book in enumerate(booklist):
            country = book["country"]
            isbn = book["isbn"]
            subtitle = book["subtitle"]
            author = book["author"]
            publisher = book["publisher"]
            price = book["price"]
            classification = book["classification"]

            self.tableWidget.insertRow(i)
            if country == "中":
                countryIcon = QIcon("./res/countries/china.png")
            elif country == "英":
                countryIcon = QIcon("./res/countries/english.png")
            elif country == "日":
                countryIcon = QIcon("./res/countries/japan.png")
            elif country == "俄":
                countryIcon = QIcon("./res/countries/russian.png")
            elif country == "美":
                countryIcon = QIcon("./res/countries/usa.png")
            else:
                countryIcon = QIcon("./res/countries/default.png")

            country_item = QTableWidgetItem(countryIcon, country)
            country_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            self.tableWidget.setItem(i, 0, country_item)

            isbn_item =QTableWidgetItem(isbn)
            isbn_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            bookname_item = QTableWidgetItem(subtitle)
            bookname_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            author_item = QTableWidgetItem(author)
            author_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            publisher_item = QTableWidgetItem(publisher)
            publisher_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            classification_item = QTableWidgetItem(classification)
            classification_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            price_item = QTableWidgetItem(price)
            price_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            self.tableWidget.setItem(i, 1, isbn_item)
            self.tableWidget.setItem(i, 2, bookname_item)
            self.tableWidget.setItem(i, 3, author_item)
            self.tableWidget.setItem(i, 4, publisher_item)
            self.tableWidget.setItem(i, 5, classification_item)
            self.tableWidget.setItem(i, 6, price_item)

    @pyqtSlot()
    def on_pushButton_addnewbook_clicked(self):
        print("1")
        bookinfo = CreateBook()
        r = bookinfo.exec_()
        if r > 0:
            self.showtable()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mb = MainBook()
    mb.show()
    sys.exit(app.exec_())



