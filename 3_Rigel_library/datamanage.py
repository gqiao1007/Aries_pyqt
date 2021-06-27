# _*_ coding: utf-8 _*_
import pickle
import os


class DataMana:

    books = []

    def loadbook(self):
        dbname = "book.dat"

        if not(os.path.exists(dbname) and os.path.isfile(dbname)):
            with open("book.dat", "wb") as f:
                pickle.dump(self.books, f)

        with open("book.dat","rb") as f:
            boooks = pickle.load(f)
        return boooks

    def insert_db(self, bookinfo):
        self.books = self.loadbook()
        for book in self.books:
            if book["isbn"] == bookinfo["isbn"]:
                return -1
        else:
            self.books.append(bookinfo)
            with open("book.dat", "wb") as f:
                pickle.dump(self.books, f)
            return 1
            # with open("book.dat", "ab+") as f:
            #     pickle.dump(bookinfo, f)
            # return 1
    def query_db(self, isbn= "", author="", bookname=""):
        self.books = self.loadbook()
        if isbn:
            for i,book in enumerate(self.books):
                if book["isbn"] == isbn:
                    return i
            else:
                return -1

        if author:
            for i,book in enumerate(self.books):
                if book["author"] == author:
                    return i
            else:
                return -1

        if bookname:
            # 按照书名查找
            for i, book in enumerate(self.books):
                if book["subtitle"] == bookname:
                    return i
            else:
                return -1

    def save_db(self, bookinfo):
        with open("book.dat", "wb") as f:
            pickle.dump(bookinfo, f)

