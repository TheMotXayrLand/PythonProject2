import logging
from datetime import date
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def log_today_date():
    today = date.today().strftime("%Y-%m-%d")
    logging.info(f"Сьогоднішня дата: {today}")
def handle_error():
    try:
        x = 1 / 0
    except Exception as e:
        logging.error(f"Сталася помилка: {e}")
def login(username, password):
    try:
        assert username == "admin" and password == "1234", "Невірне ім'я користувача або пароль"
        print("Вхід виконано успішно")
    except AssertionError as e:
        print(e)
def check_age(age):
    try:
        assert age >= 18, "Вам має бути 18 років або більше"
        print("Ви можете використовувати цей сервіс")
    except AssertionError as e:
        print(e)
def process_list(input_list):
    try:
        assert len(input_list) >= 3, "Список повинен містити принаймні 3 елементи"
        print(f"Список містить {len(input_list)} елементів")
    except AssertionError as e:
        print(e)
if __name__ == "__main__":
    log_today_date()
    handle_error()
    print("\nПеревірка логіну:")
    login("admin", "1234")
    login("user", "wrong")
    print("\nПеревірка віку:")
    check_age(20)
    check_age(16)
    print("\nПеревірка списку:")
    process_list([1, 2, 3])
    process_list([1])
