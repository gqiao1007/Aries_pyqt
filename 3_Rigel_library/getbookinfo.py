# _*_ coding: utf-8 _*_
import json
import requests

class GetBookInfo:
    def __init__(self, isbn):
        if isbn == "123":
            self.isbn = "1232456789"
        else:
            self.isbn = isbn

    def getbookinfo(self):
        # """
        # 利用豆瓣API读取图书信息
        # """
        # url = "https://api.douban.com/v2/book/isbn/:" + self.isbn
        #
        # header = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36"
        # }
        #
        # r = requests.get(url, headers=header)
        #
        # info = r.text
        #
        # bookinfo_dic = json.loads(info)
        #
        # bookinfo = {"subtitle": "", "author": "", "pubdate": "", "classification": "",
        #             "publisher": "", "price": "", "pages": "", "summary": "", "img": "", "country": ""}
        #
        # if bookinfo_dic.get("code"):
        #     rstatus = "0"
        #     # code = 0，表明我们获取数据失败
        #     return rstatus, bookinfo
        # else:
        #     rstatus = "1"
        #     subtitle = bookinfo_dic["title"]
        #     author = " ".join(bookinfo_dic["author"])
        #     pubdate = bookinfo_dic["pubdate"]
        #     classification = bookinfo_dic["tags"][0]["title"]
        #     publisher = bookinfo_dic["publisher"]
        #     price = bookinfo_dic["price"]
        #     pages = bookinfo_dic["pages"]
        #     summary = bookinfo_dic["summary"]
        #     img = bookinfo_dic["images"]["small"].replace("\\", "")
        #     if author[0] == "[":
        #         country = author[1]
        #     else:
        #         country = "中"
        #     bookinfo = {"subtitle": subtitle, "author": author, "pubdate": pubdate, "classification": classification,
        #                 "publisher": publisher, "price": price, "pages": pages, "summary": summary, "img": img,
        #                 "country": country
        #                 }
        #     return rstatus, bookinfo
            # 返回获取的状态和图书信息
        subtitle = "挪威的森林"
        author = "村上春树"
        pubdate = "1995"
        classification = "军事"
        publisher = "人民出版社"
        price = "18.00元"
        pages = "180"
        country = "中"
        img = r"\res\book\s29703778.jpg"
        summary = "那一年，是听莫扎特、钓鲈鱼和家庭破裂的一年。说到家庭破裂，母亲怪自己当初没有找到好男人，父亲则认为当时是被狐狸精迷住了眼，失常的是母亲，但出问题的是父亲……。"
        bookinfo = {"subtitle": subtitle, "author": author, "pubdate": pubdate, "classification": classification,
                         "publisher": publisher, "price": price, "pages": pages, "summary": summary, "img": img,
                         "country": country
                        }
        rstatus = 1
        return rstatus, bookinfo


