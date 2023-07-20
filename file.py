import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://www.mealty.ru/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the meal items on the page
meal_items = soup.find_all(class_="meal-popup")

# Iterate through each meal item
def new_func(meal_item):
    meal_name = meal_item.find(class_="meal-popupname").text.strip()
    return meal_name

for meal_item in meal_items:
    # Get the meal name
    meal_name = new_func(meal_item)

    # Get the portion size
    portion = meal_item.find(
        class_="meal-popupproperties-header-value meal-popupweight text-right green").text.strip()

    # Get the portion calories
    portion_calories = meal_item.find(
        class_="meal-popupproperties-header-value meal-popupcalories__portion text-right green").text.strip()

    # Get the meal price
    meal_price = meal_item.find(
        class_="meal-popupproperties-header-value meal-popupprice text-right green").text.strip()

    # Print the meal details
    print("Meal Name:", meal_name)
    print("Portion:", portion)
    print("Portion Calories:", portion_calories)
    print("Meal Price:", meal_price)
    print()
