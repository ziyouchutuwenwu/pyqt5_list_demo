#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from PyQt5 import QtWidgets
from ui.ui_list_item import Ui_widget

# 这里继承QWidget是为了setupUi的时候用，不然可以不需要
class MyWidgetCell(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWidgetCell, self).__init__(parent)

        # 使用一个恶心的方式包装
        item_cell_ui = Ui_widget()
        item_cell_ui.setupUi(self)
        self.widget = item_cell_ui.horizontalLayoutWidget
