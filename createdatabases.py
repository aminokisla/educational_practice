from bs4 import BeautifulSoup
import csv
import requests
from requests.exceptions import ConnectionError

class CreateDataBases:
    def __init__(self):
        self.rates = {}
        self.array_names = []
        self.array_counts = []
        self.array_rates = []
        try:
            url = 'https://bankiros.ru/currency/cbrf'
            res = requests.get(url=url)
            res.raise_for_status()  # Вызывает исключение, если ответ от сервера не успешный
            self.sp = BeautifulSoup(res.text, "lxml")
            self.get_num()
        except (ConnectionError, requests.HTTPError):
            print("Ошибка подключения к интернету. Данные будут загружены из последней доступной копии.")
            self.read_exchange_rates_from_csv()

    def get_num(self):
        self.rates.clear()
        self.array_names.clear()
        self.array_counts.clear()
        self.array_rates.clear()
        names = self.sp.findAll("a", class_="xxx-g-link xxx-g-link--no-bd xxx-fs-18")
        currency_counts = self.sp.findAll("div", class_="xxx-tbl-cell xxx-tbl-cell--center-v xxx-fs-18")
        currency_rates = self.sp.findAll("span", class_="xxx-fs-18")
        self.text = self.sp.find(
            class_="xxx-tbl-bottom mob:xxx-tbl-bottom--pb-0 mob:xxx-tbl-bottom--mob-p xxx-text-color-darck-gray xxx-fs-14").text
        with open("lastupdate.txt", 'w',encoding="utf-8") as file:
            file.write(self.text)
        for name in names:
            self.array_names.append(name.get_text())
        for count in currency_counts:
            self.array_counts.append(count.get_text())
        for rate in currency_rates:
            self.array_rates.append(rate.get_text())
        for i in range(4):
            self.array_rates.pop(0)
        self.write_csv()

    def write_csv(self):
        with open("all_valutes.csv", 'w', newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Count", "Rate"])
            for i in range(len(self.array_names)):
                count = self.array_counts[i]
                rate = self.array_rates[i]
                if " " in count:
                    amount, currency = count.split()
                    rate = float(rate) / float(amount)
                    count = "1 " + currency

                writer.writerow([
                    self.array_names[i],
                    count,
                    "{:.4f}".format(rate)
                ])

    def read_exchange_rates(self):
        with open('all_valutes.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                currency_code = row[1].split()[1]
                self.rates[currency_code] = float(row[2])
        self.rates["RUB"] = 1
        return self.rates

    def read_exchange_rates_from_csv(self):
        try:
            with open('all_valutes.csv', 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for row in csv_reader:
                    currency_code = row[1].split()[1]
                    self.rates[currency_code] = float(row[2])
            self.rates["RUB"] = 1
        except FileNotFoundError:
            print(
                "Файл all_valutes.csv не найден. Пожалуйста, запустите программу, когда будет доступ в интернет, чтобы загрузить актуальные данные.")

    def converter(self, input_money, input_text, output_text):
        self.read_exchange_rates()
        if input_text not in self.rates or output_text not in self.rates:
            return None
        if input_text == output_text:
            return input_money
        if input_text != "RUB" and output_text != "RUB":
            rubles = input_money * self.rates[input_text]
            return round(rubles / self.rates[output_text])
        elif input_text == "RUB":
            return round(input_money / self.rates[output_text], 2)
        elif output_text == "RUB":
            return round(input_money * self.rates[input_text], 2)