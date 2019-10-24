import requests
import openfoodfacts

# research using request
# the result ignore everything passed in the parameters except the json field.
search_result = requests.get(
    'https://world.openfoodfacts.org/',
    params={
        # 'search_terms':'Nutella',
        # 'categories':'snacks',
        # 'country':'france',
        # 'page_size':'20',
        # 'page':'1',
        'json':'1',
        },
)

for item in search_result.json()['products']:
    print(item['product_name'])

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

# research using lib

# get all categories
categories = openfoodfacts.facets.get_categories()
print(categories)

# get 20 categories
categories = openfoodfacts.facets.get_categories(
    {'country':'France'},
)
for n in range(1000):
    if categories[n]['id'].startswith('fr'):
        print(categories[n]['name'])


# get food from France from a category
products = openfoodfacts.products.get_by_facets({
  'category': 'fr:Saucissons',
  'country': 'france',
  'json':'1',
})

# get infos from food
print(products[1])                                                                              # all info products
print('product name : ', products[1]['product_name'])                                           # product name
print('picture : ', products[1]['image_front_url'])                                             # picture
print('nutriscore : ', products[1]['nutriments']['nutrition-score-fr'])                         # nutriscore
print('sugar level for 100g : ', products[1]['nutriments']['sugars_100g'])                      # sugar level for 100g
print('salt level for 100g : ', products[1]['nutriments']['salt_100g'])                         # salt level for 100g
print('carbohydrates level for 100g : ', products[1]['nutriments']['carbohydrates_100g'])       # carbohydrates level for 100g
print('sodium level for 100g : ', products[1]['nutriments']['sodium_100g'])                     # sodium level for 100g
print('saturated level for 100g : ', products[1]['nutriments']['saturated-fat_100g'])           # saturated level for 100g
print('proteins level for 100g : ', products[1]['nutriments']['proteins_100g'])                 # proteins level for 100g
print('fat level for 100g : ', products[1]['nutriments']['fat_100g'])                           # fat level for 100g

# function to return info from food
def get_infos(product):                                                                           # all info products
    return({
        'product name' : product['product_name'],
        'picture' : product['image_front_url'],
        'nutriscore' : product['nutriments']['nutrition-score-fr'],
        'sugars_100g' : product['nutriments']['sugars_100g'],
        'salt_100g' : product['nutriments']['salt_100g'],
        'carbohydrates_100g' : product['nutriments']['carbohydrates_100g'],
        'sodium_100g' : product['nutriments']['sodium_100g'],
        'saturated-fat_100g' : product['nutriments']['saturated-fat_100g'],
        'proteins_100g' : product['nutriments']['proteins_100g'],
        'fat_100g' : product['nutriments']['fat_100g'],
    })

for product in products:
    try:
        print(get_infos(product)['product name'])
    except:
        pass

# add a food in db
from fooddb.models import Food
f = Food(name='Caramel', nutriscore=3)


# a list of categories
list_of_categories = [
        'fr:Saucissons',
        'fr:Pâtes à tartiner',
        'fr:Comté',
        'fr:Charcuteries diverses',
        'fr:Jambons crus',
        'fr:Saucissons secs',
        'fr:Charcuteries cuites',
        'fr:Fromages blancs',
        'fr:miels-de-fleurs',
        'fr:Chipolatas',
        'fr:thons-a-l-huile',
        'fr:Boudins',
        'fr:Rillettes de volaille',
        'fr:Eaux-de-vie',
        'fr:purees',
        'fr:Jambons Serrano',
        'fr:Aiguillettes de poulet',
        'fr:Poulets panés',
        'fr:Reblochons',
        'fr:Allumettes de porc',
        'fr:Bloc de foie gras',
        'fr:Biscuits apéritifs soufflés',
        'fr:Miels d\'acacia',
        'fr:thons-a-l-huile-d-olive',
        'fr:Boudins blancs',
        'fr:produits-labellises',
        'fr:Tuiles salées',
        'fr:Quenelles',
        'fr:Filets d\'anchois marinés',
        'fr:Brownies',
        'Tomme',
        'fr:Fruits à coque salés',
        'fr:Filets d\'anchois marinés à l\'huile végétale',
        'fr:Céréales préparées',
        'fr:Morbiers',
        'fr:Faisselles',
        'fr:Saucissons secs pur porc',
        'fr:Ratatouilles',
        'fr:Fromages blancs natures',
        'fr:Crèmes dessert chocolat',
        'fr:Crèmes fraîches',
        'fr:Rillettes de viande rouge',
        'fr:chorizos',
        'fr:Rillettes de porc',
        'fr:Galettes à la frangipane',
        'fr:petits-beurres',
        'fr:Raclettes',
        'fr:Cordons bleus',
        'fr:Thons à l\'huile de tournesol',
        'fr:Côtes du Rhône',
        'fr:Miels crémeux',
        'fr:Brioches au chocolat',
        'fr:Crêpes de froment',
        'fr:Roqueforts',
        'fr:Bûches glacées',
        'fr:Poêlées',
        'fr:Yaourts sur lit de fruits',
        'fr:Biscuits apéritifs soufflés à base de maïs',
        'fr:aliments-a-base-de-plantes-seches',
        'fr:Pruneaux d\'Agen',
        'fr:Galettes de blé noir',
        'fr:Riz préparés',
        'fr:Fromages du Nord-Pas-de-Calais',
        'fr:Mimolettes',
        'fr:Pavés de saumon',
        'fr:escalopes-de-dinde-panees',
        'fr:palmiers',
        'fr:Saucisses sèches',
        'fr:Brandades de morue parmentière',
        'fr:Rosettes',
        'fr:Merguez',
        'fr:Nonnettes',
        'fr:Brioches pur beurre',
        'fr:escalopes-de-dinde-marinees-a-la-milanaise',
        'fr:produits-aoc',
        'fr:Crèmes entières',
        'fr:Brioches tranchées',
        'fr:confits-d-oignons',
        'fr:Desserts lactés aux œufs',
        'fr:Choucroutes garnies',
        'fr:Charcuteries à cuire',
        'fr:Coquillettes',
        'fr:Mousses de foies',
        'fr:Foies gras mi-cuits',
        'fr:Beaufort',
        'fr:Pâtes brisées',
        'fr:souris-d-agneau',
        'fr:Œufs en chocolat creux',
        'fr:Rôtis de porc',
        'fr:Tapenades noires',
        'fr:Ravioles',
        'fr:Mozzarella di Bufala Campana',
        'fr:Blinis',
        'fr:Crèmes dessert vanille',
        'fr:Cantal',
        'fr:Vinaigrettes allégées en matières grasses',
]

#for each category of the list of categories, print the name of a certain number of products from this category.
for category in list_of_categories:
    products = openfoodfacts.products.get_by_facets({
        'category': category,
        'country': 'france',
        'json':'1',
        })
    for product in products:
        try:
            print(get_infos(product)['product name'])
        except:
            pass

