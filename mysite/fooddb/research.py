from fooddb.models import Food

def display_products(research):
    for item in Food.objects.all():
        if research.lower() in str(item).lower():
            print(item, item.nutriscore)

display_products('poulet')
