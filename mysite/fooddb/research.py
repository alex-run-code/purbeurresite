from fooddb.models import Food, Category


def find_substitute(research):
    category = Category.objects.filter(food_category__food__name__icontains=research).first()
    if not category:
        return []
    print('category : ', Category)
    substitute_list = Food.objects.filter(food_category__category=category).order_by('nutriscore')
    return substitute_list
