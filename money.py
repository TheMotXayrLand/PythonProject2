import requests

class CurrencyConverter:
    def __init__(self):
        self.exchange_rate = self.get_usd_exchange_rate()

    def get_usd_exchange_rate(self):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
        try:
            response = requests.get(url)
            data = response.json()
            return data[0]["rate"]
        except Exception as e:
            print(f"Помилка отримання курсу валют: {e}")
            return None

    def convert_to_usd(self, amount_uah):
        if self.exchange_rate is None:
            print("Конвертація неможлива: немає курсу.")
            return
        amount_usd = amount_uah / self.exchange_rate
        print(f"{amount_uah:.2f} грн = {amount_usd:.2f} USD (курс {self.exchange_rate:.2f})")

# --- Основна програма ---
if __name__ == "__main__":
    try:
        amount = float(input("Введіть суму в гривнях: "))
        converter = CurrencyConverter()
        converter.convert_to_usd(amount)
    except ValueError:
        print("Будь ласка, введіть коректне числове значення.")
