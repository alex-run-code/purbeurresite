from fooddb.models import Food, Food_category, Category

def find_substitute(research):
    selection = Food.objects.filter(name__contains=research).first()
    print('selection : ', selection)
    category = Category.objects.filter(food_category__food__name=selection).first().name
    print('category : ', Category)
    substitute_list = Food.objects.filter(food_category__category__name=category).order_by('nutriscore')
    return substitute_list

# Category.objects.filter(food_category__food__name='Chiffonnade de Jambon Sec')
# Category.objects.filter(food_category__food__name='Rillettes de poulet rôti')
