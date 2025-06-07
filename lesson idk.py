import sqlite3
import requests
from datetime import datetime
import os

api_key = os.getenv('API_KEY', '5df4bde79055c2bdc82ff716510ced8b')
city = "Frydek-Mistek"
country = "CZ"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS WeatherData (
        DateTime TEXT NOT NULL,
        Temperature REAL NOT NULL
    )
''')

try:

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    if 'main' in data and 'temp' in data['main']:
        temp_now = data['main']['temp']
        print(f"Погода в {city}: {temp_now}°C")

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute('''
            INSERT INTO WeatherData (DateTime, Temperature)
            VALUES (?, ?)
        ''', (current_time, temp_now))
        conn.commit()

        print(f"Дані успішно записано: {current_time}, Температура: {temp_now}°C")
    else:
        print("Не вдалося отримати температуру з відповіді API.")

except requests.exceptions.RequestException as e:

    print(f"Ошибка при запросе данных от API: {e}")
    if response.status_code != 200:
        print(f"Ответ от API: {response.status_code} - {response.text}")
except Exception as e:

    print(f"Возникла ошибка: {e}")

finally:

    conn.close()
