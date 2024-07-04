# Задача 3
# Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны


# Убедитесь, что у вас установлены библиотеки selenium и webdriver-manager
# pip install selenium webdriver-manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

import csv

# Настройка драйвера Firefox
driver = webdriver.Firefox()

# Переход на сайт
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)
# Даем странице загрузиться
time.sleep(5)
prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")
# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Цена"])  # Запись заголовков

    for price in prices:
        writer.writerow([price.text])

# Закрытие браузера
driver.quit()

# Цены парсятся в файл prices.csv
# Файл price_kv.py обрабатывает данные и убирает руб. и сохраняет данные в cleaned_prices.csv
# grafik_price_kv.py берет данные cleaned_prices.csv составляет график и находит среднюю цену
# Файл read.me заполнен

