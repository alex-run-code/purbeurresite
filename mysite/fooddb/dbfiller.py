import requests

# research using request
search_result = requests.get(
    'https://world.openfoodfacts.org',
    params={
        'categories':'snacks',
        'country':'france',
        "page_size":"20",
        'page':'3',
        'json':'1',
        },
)

print(search_result.json()['products'][0])                                          # all info products
print(search_result.json()['products'][0]['product_name'])                          # product name
print(search_result.json()['products'][0]['image_front_url'])                       # picture
print(search_result.json()['products'][0]['nutriments']['nutrition-score-fr'])      # nutriscore
print(search_result.json()['products'][0]['nutriments']['sugars_100g'])             # sugar level for 100g
print(search_result.json()['products'][0]['nutriments']['salt_100g'])               # salt level for 100g
print(search_result.json()['products'][0]['nutriments']['carbohydrates_100g'])      # carbohydrates level for 100g
print(search_result.json()['products'][0]['nutriments']['sodium_100g'])             # sodium level for 100g
print(search_result.json()['products'][0]['nutriments']['saturated-fat_100g'])      # saturated level for 100g
print(search_result.json()['products'][0]['nutriments']['proteins_100g'])           # proteins level for 100g
print(search_result.json()['products'][0]['nutriments']['fat_100g'])                # fat level for 100g

# add a food
from fooddb.models import Food
f = Food(name='Caramel', nutriscore=3)

for item in search_result.json()['products']:
    print(item['product_name'])