from fooddb.models import Food, Food_category, Category

def find_substitute(research):
    category = Category.objects.filter(food_category__food__name__icontains=research).first()
    if not category:
        return []
    print('category : ', Category)
    substitute_list = Food.objects.filter(food_category__category=category).order_by('nutriscore')
    return substitute_list

# Category.objects.filter(food_category__food__name='Chiffonnade de Jambon Sec')
# Category.objects.filter(food_category__food__name='Rillettes de poulet rôti')
