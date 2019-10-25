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
print(products[1])                                                                           # all info products
print('product name : ', products[1]['product_name'])                                           # product name
print('picture : ', products[1]['image_front_url'])
print('off_page : ', products[1]['url'])                                           # picture
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
        'nutriscore' : product['nutriments']['nutrition-score-fr'],
        'picture' : product['image_front_url'],
        'off_url' : product['url'],
        'sugars_100g' : product['nutriments']['sugars_100g'],
        'salt_100g' : product['nutriments']['salt_100g'],
        'carbohydrates_100g' : product['nutriments']['carbohydrates_100g'],
        'sodium_100g' : product['nutriments']['sodium_100g'],
        'saturated-fat_100g' : product['nutriments']['saturated-fat_100g'],
        'proteins_100g' : product['nutriments']['proteins_100g'],
        'fat_100g' : product['nutriments']['fat_100g'],
    })

# This is a test to add a food in the database
from fooddb.models import Food
f = Food(
        name='foot test',
        nutriscore=3,
        picture_url='wewe',
        off_url='wewe',
        sugar_100g=3,
        salt_100g=3,
        carbohydrates_100g=3,
        sodium_100g=3,
        saturated_fat_100g=3,
        proteins_100g=3,
        fat_100g=3,
    )
f.save()

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

#for each category of the list of categories, add in the database the food from this category with relevent infos
for category in list_of_categories:
    products = openfoodfacts.products.get_by_facets({
        'category': category,
        'country': 'france',
        'json':'1',
        })
    for product in products:
        try:
            f = Food(
                name=product['product_name'], 
                nutriscore=product['nutriments']['nutrition-score-fr'],
                picture_url=product['image_front_url'],
                off_url=product['url'],
                sugar_100g=product['nutriments']['sugars_100g'],
                salt_100g=product['nutriments']['salt_100g'],
                carbohydrates_100g=product['nutriments']['carbohydrates_100g'],
                sodium_100g=product['nutriments']['sodium_100g'],
                saturated_fat_100g=product['nutriments']['saturated-fat_100g'],
                proteins_100g=product['nutriments']['proteins_100g'],
                fat_100g=product['nutriments']['fat_100g'],
                )
            f.save()
            print(product['product_name'], ' added')
        except:
            pass

# importing stuff
from fooddb.models import Food
from fooddb.models import Category
from fooddb.models import Food_category

# create a list then fills it with food and their respective category in the form of tuples
fc_list = []
for item in Food.objects.all():
    search_result = openfoodfacts.products.advanced_search({
    "search_terms":item.name,
    'fat':item.fat_100g,
    "country":"France",
    'json':'1',
    })
    try:
        for tag in search_result['products'][0]['categories_tags']:
            if tag.startswith('fr'):
                fc_list.append((item.name, tag))
                print(item.name, ' ', tag)
    except KeyError:
        print('key error')
              
# add each category from fc list in the database 'category'
for item in fc_list:
    try:
        c = Category(name=item[1])
        c.save()
        print(item[1], ' added')
    except:
        pass

# add in food_category database the id of the foods and their respective category
for item in fc_list:
    food_id = Food.objects.filter(name=item[0])[0]
    category_id = Category.objects.filter(name=item[1])[0]
    fc = Food_category(food_id=food_id, category_id=category_id)
    fc.save()
    print('food_id : {}, category_id : {}, added'.format(food_id, category_id))

