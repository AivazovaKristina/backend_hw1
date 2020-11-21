import datetime as dt


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        summ = 0
        for elem in self.records:
            if elem.date == dt.date.today():
                summ += elem.amount
        return summ

    def get_week_stats(self):
        summ = 0
        current_date = dt.date.today()
        last_day = current_date - dt.timedelta(days=6)
        for elem in self.records:
            if last_day <= elem.date <= current_date:
                summ += elem.amount
        return summ


class Record:
    def __init__(self, amount, comment, date=dt.date.today().strftime("%d.%m.%Y")):
        self.amount = amount
        self.date = dt.datetime.strptime(date,'%d.%m.%Y').date()
        self.comment = comment


class CashCalculator(Calculator):
    USD_RATE = 70.0
    EURO_RATE = 90.0

    def get_today_cash_remained(self, currency):
        cash = self.get_today_stats()
        USD = float(round(self.limit/self.USD_RATE-cash/self.USD_RATE, 2))
        EURO = float(round(self.limit / self.EURO_RATE - cash / self.EURO_RATE, 2))
        RUB = float(round(self.limit - cash, 2))
        if cash < self.limit:
            if currency == "usd":
                return f"На сегодня осталось {USD} USD"
            elif currency == "eur":
                return f"На сегодня осталось {EURO} Euro"
            else:
                return f"На сегодня осталось {RUB} руб"
        elif cash == self.limit:
            return "Денег нет, держись"
        else:
            if currency == "usd":
                return f"Денег нет, держись: твой долг - {abs(USD)} USD"
            elif currency == "eur":
                return f"Денег нет, держись: твой долг - {abs(EURO)} Euro"
            else:
                return f"Денег нет, держись: твой долг - {abs(RUB)} руб"


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories = self.get_today_stats()
        if self.limit > calories:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit-self.get_today_stats()} кКал"
        else:
            return "Хватит есть!"
