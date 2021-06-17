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