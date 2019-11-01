from fooddb.models import Food, Food_category, Category

def find_substitute(research):
    selection = Food.objects.filter(name__contains=research).first()
    category = Category.objects.filter(food_category__food__name=selection).first().name
    substitute_list = Food.objects.filter(food_category__category__name=category).order_by('nutriscore')
    return substitute_list

