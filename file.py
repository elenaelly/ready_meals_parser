import requests
from bs4 import BeautifulSoup

url = 'https://mealty.ru/'
html = requests.get(url, timeout=10)
soup = BeautifulSoup(html.text, 'html.parser')

meal_names = soup.find_all("div", class_="meal-card__name")

meal_notes = soup.find_all("div", class_="meal-card__name-note")

meal_prices = soup.find_all("span", class_="basket__footer-total-count green")

meal_calories = soup.find_all("div", class_="meal-card__calories__portion")

meal_sizes = soup.find_all("div", class_="meal-card__weight")

for meal_name, meal_note, meal_price, meal_calorie, meal_size in zip(meal_names, meal_notes, meal_prices, meal_calories, meal_sizes):
    name = meal_name.get_text()
    note = meal_note.get_text()
    price = meal_price.get_text()
    calories = meal_calorie.get_text()
    size = meal_size.get_text()

    print(f'{name} {note}. Цена: {price} руб. Калории: {calories} на {size} гр.')
    #print(f'{name} {note};{price};{calories};{size}')
