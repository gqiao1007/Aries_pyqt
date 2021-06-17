# _*_ coding: utf-8 _*_

from PyQt5.QtWidgets import QListView, QMenu, QAction, QMessageBox
from ListModel import ListModel

class ListView(QListView):
    map_ListView = []
    def __init__(self):
        super().__init__()
        self.m_pModel = ListModel()
        self.setModel(self.m_pModel)

    def contextMenuEvent(self, event):
        hitIndex = self.indexAt(event.pos()).column()

        if hitIndex > -1:
            # 找到索引
            pmenu = QMenu(self)
            pDeleteAct = QAction("删除", pmenu)
            pmenu.addAction(pDeleteAct)
            pDeleteAct.triggered.connect(self.deleteItemSlot)
            pSubMenu = QMenu("转移联系人至", pmenu)
            pmenu.addMenu(pSubMenu)
            for item_dic in self.map_listview:
                # 这里我们将每个分组名称取出，新建一个QAction对象，加入到pSubMenu当中。
                pMoveAct = QAction(item_dic['groupname'], pmenu)
                pSubMenu.addAction(pMoveAct)
                pMoveAct.triggered.connect(self.move)
                # 点击这个每个分组的时候就会执行联系人转移分组操作，这里就是move()的调用。
            pmenu.popup(self.mapToGlobal(event.pos()))

    def deleteItemSlot(self):
        '''
        删除联系人
        '''
        index = self.currentIndex().row()
        if index > -1:
            self.m_pModel.deleteItem(index)

    def setListMap(self, listview):
        '''
        将分组名称和QListView对象这个字典增加到map_listview数据列表中
        '''
        self.map_listview.append(listview)

    def move(self):
        '''
        实现联系人转移
        '''
        tolistview = self.find(self.sender().text())
        # 点击的分组名称找到对应的QListView对象

        if tolistview is self:
            prelistview = self.sender().text()
            QMessageBox.warning(self, "警告", "该联系人就在{}，还怎么移动啊！".format(prelistview))
            # 假设联系人就在将转移的分组，那我们就没有必要转移了
        else:
            index = self.currentIndex().row()
            pItem = self.m_pModel.getItem(index)
            tolistview.addItem(pItem)
            self.m_pModel.deleteItem(index)
            # 否则我们首先要获得这个联系人，然后在将转移的分组中将这个联系人加上，原分组联系人删除

    def find(self, pmenuname):
        '''
        找到分组对象
        '''
        for item_dic in self.map_listview:
            if item_dic['groupname'] == pmenuname:
                return item_dic['listview']
