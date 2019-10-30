from fooddb.models import Food, Food_category

def display_products(research):
    research_result = []
    for item in Food.objects.all():
        if research.lower() in str(item).lower():
            research_result.append(item.name)
    return(research_result)

display_products('poulet')

def find_substitute(selection):
    selection_id = Food.objects.filter(name=selection)[0].id
    category_of_selection_id = Food_category.objects.filter(food=selection_id)[0].category_id
    food_from_same_category = []
    for item in Food_category.objects.filter(category=category_of_selection_id):
        food_from_same_category.append(item.food)
    substitute_list = []
    for item in food_from_same_category:
        for food in Food.objects.filter(name=item):
            substitute_list.append((food.name,food.nutriscore))
            substitute_list_sorted = sorted(substitute_list, key=lambda tup: (tup[1]))
    substitute_name = substitute_list_sorted[0][0]
    substitute_nutriscore = substitute_list_sorted[0][1]
    print(substitute_name, substitute_nutriscore)

find_substitute('Rillettes de poulet rôti')