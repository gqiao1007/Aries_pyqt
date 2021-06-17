# _*_ coding: utf-8 _*_
import random
import Random_Name
from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex, QVariant, QSize
from PyQt5.QtGui import QIcon, QFont


class ListModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.ListItemData = []

        self.Data_init()

    def Data_init(self):
        randomnum = random.sample(range(26), 10)
        for i in randomnum:
            username = Random_Name.getname()
            ItemData = {'name': '', 'iconPath': ''}
            ItemData['name'] = username
            ItemData['iconPath'] = "./res/"+ str(i) + ".jpg"
            self.ListItemData.append(ItemData)

    def rowCount(self, parent=QModelIndex()):
        return len(self.ListItemData)

    # def data(self, index, role=None):
    #     if index.isVaild() or (0 < index.row() < len(self.ListItemData())):
    #         if role == Qt.DisplayRole:
    #             return QVariant(self.ListItemData[index.row()]['name'])
    #             # 文本形式呈现数据
    #         elif role == Qt.DecorationRole:
    #             return QVariant(QIcon(self.ListItemData[index.row()]['iconPath']))
    #             # 以图标形式呈现装饰数据
    #         elif role == Qt.SizeHintRole:
    #             return QVariant(QSize(70, 80))
    #             # 视图项目大小
    #         elif role == Qt.TextAlignmentRole:
    #             return QVariant(int(Qt.AlignHCenter | Qt.AlignVCenter))
    #             # 文本对齐方式
    #         elif role == Qt.FontRole:
    #             font = QFont()
    #             font.setPixelSize(20)
    #             return QVariant(font)
    #             # 字体设置
    #     return QVariant()

    def addItem(self, itemData):
        if itemData:
            self.beginInsertRows(QModelIndex(), len(self.ListItemData), len(self.ListItemData) + 1)
            self.ListItemData.append(itemData)
            self.endInsertRows()

    def deleteItem(self, index):

        del self.ListItemData[index]

    def getItem(self, index):
        if index > -1 and index < len(self.ListItemData):
            return self.ListItemData[index]



