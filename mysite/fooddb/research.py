from fooddb.models import Food, Category


def find_substitute(research):
    """
    Research in the database the foods from the same
    category than user's research. Then return a list
    of substitues ordered by nutriscore.
    """
    category = Category.objects.filter(food_category__food__name__icontains=research).first()
    if not category:
        return []
    substitute_list = Food.objects.filter(food_category__category=category).order_by('nutriscore')
    return substitute_list
