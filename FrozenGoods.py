from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import FindItem
import AddToCart
import Checkout
import sys
import pymysql

class FrozenGoods(QWidget):

    def __init__(self, username, store_id, order_id):
        super(FrozenGoods, self).__init__()
        self.username = username
        self.store_id = store_id
        self.order_id = order_id
        self.food_group = FrozenGoods
        self.qButtonGroup = QButtonGroup()
        self.connection = pymysql.connect(host='localhost',
                                     user = 'root',
                                     password=None,
                                     db = 'GroceryTech',
                                     charset = 'utf8mb4')


        self.initUI()

    def initUI(self):

        #setLayout
        root = QVBoxLayout()
        bottom = QHBoxLayout()


        #widgets

        self.back = QPushButton("Back")
        self.addtocart = QPushButton("Add to Cart")
        self.checkout = QPushButton("Checkout")
        self.frozengoodstable = self.populate()

        bottom.addWidget(self.back)
        bottom.addWidget(self.addtocart)
        bottom.addWidget(self.checkout)

        self.back.clicked.connect(self.backClicked)
        self.addtocart.clicked.connect(self.addtoCartClicked)
        self.checkout.clicked.connect(self.checkOutClicked)

        root.addWidget(self.frozengoodstable)
        root.addLayout(bottom)
        self.setLayout(root)
        self.setWindowTitle("Frozen Goods")
        self.setGeometry(550, 450, 600, 300)



        self.show()


    def backClicked(self):
        self.connection.close()

        self.FindItem = FindItem.FindItem(self.username, self.store_id, self.order_id)
        self.FindItem.show()
        self.close()


    def addtoCartClicked(self):
        numRow = self.getRowCount()
        item_IDs = self.getItemIDs()

        for i in range(numRow):
            currrent_value = int(self.bakinggoodstable.item(i, 0).text())

            if currrent_value != 0:
                AddToCart.addToCart(self.order_id, item_IDs[i], currrent_value)

    def checkOutClicked(self):
        self.connection.close()

        self.checkOutWin = Checkout.Checkout(self.username, self.store_id, self.order_id)
        self.checkOutWin.show()
        self.close()

    def populate(self):

        frozengoodstable = QTableWidget()
        frozengoodstable.setRowCount(self.getRowCount())
        frozengoodstable.setColumnCount(6)
        frozengoodstable.setHorizontalHeaderLabels(['Quantity','Item Name', 'Description','Expiration Date','Price','In Stock'])

        item_IDs = self.getItemIDs()

        for i in range(self.getRowCount()):
            print(str(self.getRowCount()))
            spinBox = QSpinBox()
            frozengoodstable.setCellWidget(i, 0, spinBox)

            for j in range(5):

                if j == 0:
                    itemName = QTableWidgetItem(self.getItemName(item_IDs[i]))
                    itemName.setTextAlignment(Qt.AlignCenter)
                    itemName.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                    frozengoodstable.setItem(i, 1, itemName)

                if j == 1:
                    description = QTableWidgetItem(self.getDescription(item_IDs[i]))
                    description.setTextAlignment(Qt.AlignCenter)
                    description.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                    frozengoodstable.setItem(i, 2, description)

                if j == 2:
                    quantity = QTableWidgetItem(str(self.getExpDate(item_IDs[i])))
                    quantity.setTextAlignment(Qt.AlignCenter)
                    quantity.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                    frozengoodstable.setItem(i, 3, quantity)

                if j == 3:
                    retailPrice = QTableWidgetItem(str(self.getRetailPrice(item_IDs[i])))
                    retailPrice.setTextAlignment(Qt.AlignCenter)
                    retailPrice.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                    frozengoodstable.setItem(i, 4, retailPrice)

                if j == 4:
                    expDate = QTableWidgetItem(str(self.getQuantity(item_IDs[i])))
                    expDate.setTextAlignment(Qt.AlignCenter)
                    expDate.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                    frozengoodstable.setItem(i, 6, expDate)

        return frozengoodstable

    def getRowCount(self):
        cursor = self.connection.cursor()
        numofRows = 'select count(*) from item, soldat where item.item_id=soldat.item_id and food_group="Frozen Goods" and soldat.store_id={};'.format(self.store_id)
        cursor.execute(numofRows)
        return cursor.fetchone()[0]


    def getItemIDs(self):
        cursor = self.connection.cursor()

        select = ('SELECT item.item_id FROM ITEM, SOLDAT WHERE item.item_id = soldat.item_id and food_group = "Frozen Goods" and soldat.store_id={};'.format(self.store_id))
        cursor.execute(select)
        found = cursor.fetchall()


        item_IDs = []
        for num in found:
            item_IDs.append(num[0])

        return item_IDs

    def getExpDate(self, item_id):
        cursor = self.connection.cursor()

        select = ('SELECT item.exp_date FROM ITEM WHERE food_group = "Frozen Goods" and item_id={};'.format(item_id))
        cursor.execute(select)
        return cursor.fetchone()[0]

    def getItemName(self, item_id):
        cursor = self.connection.cursor()

        select = ('SELECT item.item_name FROM ITEM WHERE food_group = "Frozen Goods" and item_id={};'.format(item_id))
        cursor.execute(select)
        return cursor.fetchone()[0]

    def getRetailPrice(self, item_id):
        cursor = self.connection.cursor()

        select = ('SELECT item.listed_price FROM ITEM WHERE food_group = "Frozen Goods" and item_id={};'.format(item_id))
        cursor.execute(select)
        return cursor.fetchone()[0]

    def getDescription(self, item_id):
        cursor = self.connection.cursor()

        select = ('SELECT item.description FROM ITEM WHERE food_group = "Frozen Goods" and item_id={};'.format(item_id))
        cursor.execute(select)
        return cursor.fetchone()[0]

    def getQuantity(self, item_id):
        cursor = self.connection.cursor()

        select = ('SELECT item.quantity FROM ITEM WHERE food_group = "Frozen Goods" and item_id={};'.format(item_id))
        cursor.execute(select)
        if cursor.fetchone()[0] > 0:
            return 'Yes'
        else:
            return 'No'





        #help populate Frozen Goods
        #select grocerystore.store_id, store_name, item_name from item, grocerystore, soldat where food_group="Frozen Goods" and soldat.store_id=grocerystore.store_id and item.item_id=soldat.item_id;
