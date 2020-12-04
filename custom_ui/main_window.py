#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListWidgetItem
from custom_ui.my_widget_cell import MyWidgetCell
from ui.ui_window import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        list_item = QListWidgetItem()
        list_item.setSizeHint(QSize(279, 50))
        item_widget_cell = MyWidgetCell()
        self._list.addItem(list_item)
        self._list.setItemWidget(list_item, item_widget_cell.widget)
