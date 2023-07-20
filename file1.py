import requests
from bs4 import BeautifulSoup

# Отправляем GET-запрос на страницу
url = "https://www.mealty.ru/"
response = requests.get(url)

# Создаем объект BeautifulSoup для парсинга HTML-кода страницы
soup = BeautifulSoup(response.content, 'html.parser')

# Находим все блоки с информацией о блюдах
meal_blocks = soup.find_all(class_='meal-popup')

# Проходимся по каждому блоку и получаем нужные данные
for meal_block in meal_blocks:
    # Парсим название блюда
    meal_name = meal_block.find(class_='meal-popupname').text
    # Парсим вес порции
    portion = meal_block.find(class_='meal-popupproperties-header-value meal-popupweight text-right green').text
    # Парсим количество калорий порции
    portion_calories = meal_block.find(class_='meal-popupproperties-header-value meal-popupcalories__portion text-right green').text
    # Парсим цену блюда
    meal_price = meal_block.find(class_='meal-popupproperties-header-value meal-popupprice text-right green').text
    
    # Выводим полученные данные
    print('Название блюда:', meal_name)
    print('Вес порции:', portion)
    print('Количество калорий в порции:', portion_calories)
    print('Цена:', meal_price)
    print('---')