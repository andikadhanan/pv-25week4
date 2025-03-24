from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 60, 491, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(50, -1, 100, 25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        
        self.productBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.productBox.setObjectName("productBox")
        self.productBox.addItems(["", "Bimoli (Rp 20.000)", "Beras 5 Kg (Rp 75.000)", "Kecap XYZ (Rp 7.000)", "Saos Tiram (Rp 10.000)"])
        self.horizontalLayout.addWidget(self.productBox)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(50, -1, 100, 25)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        
        self.quantityBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.quantityBox.setObjectName("quantityBox")
        self.horizontalLayout_3.addWidget(self.quantityBox)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(50, -1, 100, 25)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        
        self.discountBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.discountBox.setObjectName("discountBox")
        self.discountBox.addItems(["0%", "5%", "10%", "15%"])
        self.horizontalLayout_2.addWidget(self.discountBox)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(120, -1, 120, 30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.btnAddCart = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnAddCart.setObjectName("btnAddCart")
        self.horizontalLayout_4.addWidget(self.btnAddCart)
        
        self.btnClear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout_4.addWidget(self.btnClear)
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.btnAddCart.clicked.connect(self.add_to_cart)
        self.btnClear.clicked.connect(self.clear_cart)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Shopping Cart"))
        self.label.setText(_translate("MainWindow", "Product"))
        self.label_3.setText(_translate("MainWindow", "Quantity"))
        self.label_2.setText(_translate("MainWindow", "Discount"))
        self.btnAddCart.setText(_translate("MainWindow", "Add to Cart"))
        self.btnClear.setText(_translate("MainWindow", "Clear"))
        self.label_4.setText(_translate("MainWindow", "Total: Rp 0"))
    
    def add_to_cart(self):
        products = {"Bimoli (Rp 20.000)": 20000, "Beras 5 Kg (Rp 75.000)": 75000, "Kecap XYZ (Rp 7.000)": 7000, "Saos Tiram (Rp 10.000)": 10000}
        
        product = self.productBox.currentText()
        quantity = self.quantityBox.value()
        discount = int(self.discountBox.currentText().replace('%', ''))
        
        if product and quantity > 0:
            price = products[product] * quantity
            discount_amount = price * (discount / 100)
            final_price = price - discount_amount
            
            self.listWidget.addItem(f"{product} x{quantity} - Rp {final_price:,.0f}")
            
            total = sum(float(item.text().split('- Rp ')[1].replace(',', '')) for item in self.listWidget.findItems("*", QtCore.Qt.MatchWildcard))
            self.label_4.setText(f"Total: Rp {total:,.0f}")
    
    def clear_cart(self):
        self.listWidget.clear()
        self.label_4.setText("Total: Rp 0")
