

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("CurrencyConverter")
        MainWindow.resize(490, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #838383")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 100, 261, 111))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 90, 41, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Снимок экрана 2024-04-27 094601.png"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(50, 250, 170, 60))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background-color: #838383;\n"
"border: 4px solid #8ccaca;\n"
"border-radius: 30;\n"
"color: white")
        self.input_currency.setText("")
        self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(270, 250, 170, 60))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background-color: #838383;\n"
"border: 4px solid #8ccaca;\n"
"border-radius: 30;\n"
"color: white")
        self.output_currency.setText("")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.input_amount_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount_2.setGeometry(QtCore.QRect(140, 360, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.input_amount_2.setFont(font)
        self.input_amount_2.setStyleSheet("background-color: #838383;\n"
"border: 4px solid #8ccaca;\n"
"border-radius: 30;\n"
"color: white")
        self.input_amount_2.setText("")
        self.input_amount_2.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount_2.setObjectName("input_amount_2")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(140, 580, 200, 60))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background-color: #838383;\n"
"border: 4px solid #8ccaca;\n"
"border-radius: 30;\n"
"color: white")
        self.output_amount.setText("")
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 470, 170, 60))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    background-color: #8ccaca;\n"
"    border-radius: 30;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #388685\n"
"}")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "currency converter"))
        self.pushButton.setText(_translate("MainWindow", "CONVERT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
