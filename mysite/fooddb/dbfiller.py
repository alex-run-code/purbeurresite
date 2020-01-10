import openfoodfacts
from fooddb.models import Food, Category, Food_category

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

fc_list = []


def add_food_in_db():
    '''
    For each category of list_of_categories,
    add in the database a certain number of foods
    with relevent informations
    '''
    for category in list_of_categories:
        products = openfoodfacts.products.get_by_facets({
            'category': category,
            'country': 'france',
            'json': '1',
            })
        for product in products:
            try:
                f = Food(
                    name=product['product_name'],
                    nutriscore=product['nutriscore_grade'],
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


def fc_list_filler():
    '''
    look at foods in our database and their respective category
    in OFF's database, then fills fc_list with the foods and their
    respective category in the form of tuples
    '''
    for item in Food.objects.all():
        search_result = openfoodfacts.products.advanced_search({
            "search_terms": item.name,
            'fat': item.fat_100g,
            "country": "France",
            'json': '1',
            })
        try:
            for tag in search_result['products'][0]['categories_tags']:
                if tag.startswith('fr'):
                    fc_list.append((item.name, tag))
                    print(item.name, ' ', tag)
        except KeyError:
            print('key error')
        except IndexError:
            print('Index Error')


def add_categories_in_db():
    '''
    add each category from fc list in the database 'category'
    '''
    # for item in fc_list:
    for item in fc_list:
        try:
            c = Category(name=item[1])
            c.save()
            print(item[1], ' added')
        except:
            pass


def fills_fc_database():
    '''
    Add in Food_category database the id of
    the foods and their category
    '''
    # for item in fc_list:
    for item in fc_list:
        try:
            food_id = Food.objects.filter(name=item[0])[0]
            category_id = Category.objects.filter(name=item[1])[0]
            fc = Food_category(food=food_id, category=category_id)
            fc.save()
            print('food_id : {}, category_id : {}, added'.format(food_id, category_id))
        except:
            pass


add_food_in_db()
fc_list_filler()
add_categories_in_db()
fills_fc_database()
