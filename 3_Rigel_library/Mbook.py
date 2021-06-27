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
        #真实行数
        list_rows = len(self.booklist)
        #table_rows 当前行数
        table_rows = self.tableWidget.rowCount()

        if table_rows == 0 and list_rows > 0:
             self.selectTable(self.booklist)

        if table_rows >0 and list_rows > 0:
            self.tableWidget.clear()
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

    @pyqtSlot(int, int)
    def on_tableWidget_cellClicked(self, row, column):
        self.label_country.setText(self.booklist[row]["country"])
        self.label_ISBN.setText(self.booklist[row]["isbn"])
        self.label_bookname.setText(self.booklist[row]["subtitle"])
        self.label_author.setText(self.booklist[row]["author"])
        self.label_present.setText(self.booklist[row]["publisher"])
        self.label_price.setText(self.booklist[row]["price"])
        self.label_Pyear.setText(self.booklist[row]["pubdate"])
        self.label_pagenum.setText(self.booklist[row]["pages"])
        self.textBrowser.setText(self.booklist[row]["summary"])
        img = self.booklist[row]["img"]
        imgname = './res/book/' + img.split("/")[-1]
        self.label.setPixmap(QPixmap(imgname))
        self.label.setScaledContents(True)

    @pyqtSlot()
    def on_pushButton_search_clicked(self):
        searchtext = self.lineEdit.text()
        if searchtext:
            if self.comboBox.currentText() == "ISBN":
                index = self.bookdb.query_db(isbn=searchtext)
            elif self.comboBox.currentText() == "书名":
                index = self.bookdb.query_db(bookname=searchtext)
            elif self.comboBox.currentText() == "作者":
                print("1", searchtext)
                index = self.bookdb.query_db(author=searchtext)
            if index > -1:
                self.tableWidget.selectRow(index)
            else:
                QMessageBox.information(self, "提示", "Sorry。貌似没有找到你要的书，换个词试试吧！")
        else:
            QMessageBox.information(self,"提示", "没有关键词！")

    @pyqtSlot()
    def on_pushButton_save_clicked(self):

        pass

    @pyqtSlot(int, int)
    def on_tableWidget_cellDoubleClicked(self, row, column):

        if column == 0:
            # countries = ["中", "英", "日", "俄", "美"]
            com_country = QComboBox()

            com_country.addItem(QIcon("./res/countries/china.png"),"中")
            com_country.addItem(QIcon("./res/countries/english.png"),"英")
            com_country.addItem(QIcon("./res/countries/japan.png"),"日")
            com_country.addItem(QIcon("./res/countries/russian.png"),"俄")
            com_country.addItem(QIcon("./res/countries/usa.png"),"美")
            old_classification = self.booklist[row]["country"]
            com_country.setCurrentText(old_classification)
            self.tableWidget.setCellWidget(row, 0, com_country)
            # com_country.setEditable(False)

        if column == 5:
            com = QComboBox()
            classifications = ["", "马克思主义、列宁主义、毛泽东思想、邓小平理论", "哲学、宗教", "社会科学总论",
            "政治、法律", "军事", "经济", "文化、科学、教育、体育", "语言、文字", "文学",
            "艺术", "历史、地理", "自然科学总论", "数理科学和化学", "天文学、地球科学", "生物科学",
            "医药、卫生", "农业科学", "工业技术", "交通运输", "航空、航天", "环境科学、劳动保护科学（安全科学）",
            "综合性图书"]
            com.addItems(classifications)
            # com.setEditable(True)
            old_classification = self.booklist[row]["classification"]
            com.setCurrentText(old_classification)
            self.tableWidget.setCellWidget(row,5,com)
        self.pushButton_save.setEnabled(True)

    @pyqtSlot(int, int, int, int)
    def on_tableWidget_currentCellChanged(self, currentRow, currentColumn, previousRow, previousColumn):
        """
        :param currentRow:  当面选中坐标行
        :param currentColumn:
        :param previousRow:
        :param previousColumn:
        :return:
        """
        if previousColumn == 1:
            isbn = self.tableWidget.item(previousRow, previousColumn).text()
            self.booklist[previousRow]["isbn"] = isbn
        if previousColumn == 2:
            bookname = self.tableWidget.item(previousRow, previousColumn).text()
            self.booklist[previousRow]["subtitle"] = bookname
        if previousColumn == 3:
            author = self.tableWidget.item(previousRow, previousColumn).text()
            self.booklist[previousRow]["author"] = author
        if previousColumn == 4:
            publisher = self.tableWidget.item(previousRow, previousColumn).text()
            self.booklist[previousRow]["publisher"] = publisher
        if previousColumn == 6:
            price = self.tableWidget.item(previousRow, previousColumn).text()
            self.booklist[previousRow]["price"] = price

        else:
            previous_item = self.tableWidget.cellWidget(previousRow, previousColumn)
            if previous_item:
                clt = previous_item.currentText()
                self.tableWidget.removeCellWidget(previousRow, previousColumn)
                if previousColumn == 5:
                    cl = QTableWidgetItem(clt)
                    cl.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(previousRow, 5, cl)
                    self.booklist[previousRow]["classification"] = clt

                if previousColumn == 0:
                    if clt == "中":
                        countryIcon = QIcon("./res/countries/china.png")
                    elif clt == "英":
                        countryIcon = QIcon("./res/countries/english.png")
                    elif clt == "日":
                        countryIcon = QIcon("./res/countries/japan.png")
                    elif clt == "俄":
                        countryIcon = QIcon("./res/countries/russian.png")
                    elif clt == "美":
                        countryIcon = QIcon("./res/countries/usa.png")
                    else:
                        countryIcon = QIcon("./res/countries/default.png")

                    country_item = QTableWidgetItem(countryIcon, clt)
                    country_item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(previousRow, 0, country_item)
                    # 修改国家时，我们会调出国家的下拉框供选择
                    self.booklist[previousRow]["country"] = clt

    @pyqtSlot()
    def on_pushButton_save_clicked(self):

        self.bookdb.save_db(self.booklist)
        QMessageBox.information(self, "提示", "保存成功！")
        self.pushButton_save.setEnabled(False)

    # def contextMenuEvent(self, event):
    #     pmenu = QMenu
    #     pdeleAct = QAction("删除行", self.tableWidget)
    #     pmenu.addAction(pdeleAct)
    #     pdeleAct.triggered.connect(self.)










if __name__ == "__main__":
    app = QApplication(sys.argv)
    mb = MainBook()
    mb.show()
    sys.exit(app.exec_())



