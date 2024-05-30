import csv
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget, QComboBox,QHBoxLayout
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import Qt
from createdatabases import CreateDataBases


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.database = CreateDataBases()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Конвертер валют")
        self.resize(400, 200)
        main_layout = QVBoxLayout()
        source_currency_layout = QHBoxLayout()
        source_label = QLabel("Исходная валюта:")
        self.input_currency = QComboBox(self)

        source_currency_layout.addWidget(source_label)
        source_currency_layout.addWidget(self.input_currency)
        main_layout.addLayout(source_currency_layout)

        amount_layout = QHBoxLayout()
        amount_label = QLabel("Сумма:")
        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Введите сумму")
        validator = QDoubleValidator(0.0, 1e9, 2, self)
        validator.setNotation(QDoubleValidator.Notation.StandardNotation)
        self.amount_input.setValidator(validator)

        amount_layout.addWidget(amount_label)
        amount_layout.addWidget(self.amount_input)
        main_layout.addLayout(amount_layout)

        target_currency_layout = QHBoxLayout()
        target_label = QLabel("Целевая валюта:")
        self.output_currency = QComboBox(self)

        target_currency_layout.addWidget(target_label)
        target_currency_layout.addWidget(self.output_currency)
        main_layout.addLayout(target_currency_layout)

        # Кнопка для конвертации
        self.convert_button = QPushButton("Конвертировать", self)
        self.convert_button.clicked.connect(self.convert)

        main_layout.addWidget(self.convert_button, alignment=Qt.AlignmentFlag.AlignCenter)

        # Метка для отображения результата
        self.result_label = QLabel("Результат конвертации")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.result_label)

        self.central_widget = QWidget()
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)
        self.load_currencies_from_csv()

    def load_currencies_from_csv(self):
        currencies = set(["RUB"])
        with open('all_valutes.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                currency_code = row[1].split()[1]
                currencies.add(currency_code)
        for currency in sorted(currencies):
            self.input_currency.addItem(currency)
            self.output_currency.addItem(currency)

    def convert(self):
        try:
            amount = float(self.amount_input.text())
        except ValueError:
            self.result_label.setText("Ошибка: введите число в поле суммы")
            return

        input_currency = self.input_currency.currentText()
        output_currency = self.output_currency.currentText()

        result = self.database.converter(amount, input_currency, output_currency)
        if result is not None:
            self.result_label.setText(f"Результат: {result} {output_currency}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
            QPushButton {
                background-color: #8ccaca;
                color: white;
                font-weight:bold;
                border-radius: 15px;
                padding: 10px 25px;
                font-size: 20px;
                text-align: center;
                margin: 10px 0;
                outline: none;
                box-shadow: 0 4px 6px 0 rgba(0,0,0,0.2);
                transition: background-color 0.3s, box-shadow 0.3s;
            }
            QPushButton:hover {
                background-color: #388685;
                box-shadow: 0 4px 6px 0 rgba(0,0,0,0.3);
            }
            QLineEdit, QComboBox,QLabel {
                padding: 5px;
                min-height: 34px; /* Установка минимальной высоты, соответствующей QComboBox */
                font-size: 17px; /* Установка размера шрифта, соответствующего QComboBox */
                margin: 5px 0;
                font-weight:bold;
                border: 3px solid #8ccaca;
                border-radius: 15px;
            }
            QComboBox {
                border: 1px solid #ced4da;
                border-radius: 4px;
                padding: 5px;
                font-size: 14px;
                min-height: 34px;
                background-color: #ffffff;
                selection-background-color: #6c757d;
            }
            
            QComboBox:hover {
                border: 1px solid #adb5bd;
            }
            
            QComboBox:pressed, QComboBox::drop-down:pressed {
                background-color: #ffffff;
            }
            
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px;
                border-left-width: 1px;
                border-left-color: #adb5bd;
                border-left-style: solid;
                border-top-right-radius: 4px;
                border-bottom-right-radius: 4px;
            }
            
            QComboBox::down-arrow {
                width: 16px;
                height: 16px;
                image: url('2.png');
                border-image: url('2.png') 0 stretch; /* Говорит, что изображение не нужно обрезать и его можно растягивать */
            }
            
            QComboBox QAbstractItemView {
                border: 1px solid #adb5bd;
                selection-background-color: #6c757d;
                padding: 10px;
                background: #ffffff;
            }
            QLineEdit:focus, QComboBox:focus {
                border: 1px solid #777;
            }
            QLabel {
                font-size: 17px;
                font-weight:bold;

            }
            QMainWindow {
                background-color: #838383;
            }
        """)
    window = MainWindow()
    window.show()
    app.exec()
