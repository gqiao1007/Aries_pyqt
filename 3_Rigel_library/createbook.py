# _*_ coding: utf-8 _*_

from PyQt5.QtWidgets import QDialog, QMessageBox, QFileDialog
from ui_addnewbook import Ui_Dialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from getbookinfo import GetBookInfo
from PyQt5.QtGui import QPixmap
import sys


class CreateBook(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(CreateBook,self).__init__(parent)
        self.setupUi(self)
        self.initUI()

        self.isbn = ""
        self.bookname = ""
        self.author = ""
        self.year = ""
        self.present = ""
        self.classification = ""
        self.price = ""
        self.pages = ""
        self.summary = ""
        self.img = ""
        self.country = ""
        self.header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
        }

    def initUI(self):
        classifications = ["", "马克思主义、列宁主义、毛泽东思想、邓小平理论", "哲学、宗教", "社会科学总论",
                    "政治、法律", "军事", "经济", "文化、科学、教育、体育", "语言、文字", "文学",
                    "艺术", "历史、地理", "自然科学总论", "数理科学和化学", "天文学、地球科学", "生物科学",
                    "医药、卫生", "农业科学", "工业技术", "交通运输", "航空、航天", "环境科学、劳动保护科学（安全科学）",
                    "综合性图书"]
        self.comboBox.addItems(classifications)

        self.button_read_internet
    @pyqtSlot()
    def on_button_read_internet_clicked(self):
        self.isbn = self.lineEdit_isbn.text()
        if self.isbn == "":
            QMessageBox.warning(self, "Warning", "ISBN is None")
            self.lineEdit_isbn.setFocus()
        else:
            book = GetBookInfo(self.isbn)
            restaus, bookinfo = book.getbookinfo()

            if restaus == 1:
                self.subtitle = bookinfo["subtitle"]
                self.author = bookinfo["author"]
                self.pubdate = bookinfo["pubdate"]
                self.classification = bookinfo["classification"]
                self.publisher = bookinfo["publisher"]
                self.price = bookinfo["price"]
                self.pages = bookinfo["pages"]
                self.summary = bookinfo["summary"]
                self.img = bookinfo["img"]
                self.country = bookinfo["country"]
                self.set_bookinfo()
            else:
                QMessageBox.warning(self, "警告", "大兄dei貌似查不到哦")
                self.lineEdit_isbn.setFocus()

    @pyqtSlot()
    def on_pushButton_selectbook_clicked(self):
        """
        选图书封面
        :return:
        """
        pass
    def set_bookinfo(self):
        self.lineEdit_bookname.setText(self.subtitle)
        self.lineEdit_author.setText(self.author)
        self.comboBox.setEditText(self.classification)
        self.lineEdit_present.setText(self.publisher)
        self.lineEdit_page.setText(self.pages)
        self.lineEdit_price.setText(self.price)
        self.textEdit.setPlainText(self.summary)
        self.lineEdit_year.setText(self.pubdate)

        imgname = './res/book/' + self.img.split("\\")[-1]
        print(imgname)
        self.label_pixmap.setPixmap(QPixmap(imgname))
    @pyqtSlot()
    def on_pushButton_selectbook_clicked(self):
        """
        图书封面选择
        :return:
        """
        f = QFileDialog.getOpenFileName(self, "选择图书封面", "./res/book/", ("Images (*.png *.jpg)"))
        if f[0]:
            self.label_pixmap.setPixmap(QPixmap(f[0]))
            self.img = f[0]









if __name__ == "__main__":
    app = QApplication(sys.argv)
    mb = CreateBook()
    mb.show()
    sys.exit(app.exec_())
