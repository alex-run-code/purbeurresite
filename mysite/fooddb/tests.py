from django.test import TestCase
from fooddb.research import find_substitute
from fooddb.models import Category, Food, Food_category

# Create your tests here.
class FindSubstituteTest(TestCase):

    def setUp(self):
        food1 = Food(name='poulet aux petits pois',nutriscore='b')
        food1.save()
        food2 = Food(name='poulet braisé',nutriscore='c')
        food2.save()
        food3 = Food(name='nuggets de poulet',nutriscore='d')
        food3.save()
        food4 = Food(name='glace à la fraise',nutriscore='c')
        food4.save()
        category1 = Category(name="viande")
        category1.save()
        category2 = Category(name="dessert")
        category2.save()
        fc1 = Food_category(food=food1, category=category1)
        fc1.save()
        fc2 = Food_category(food=food2, category=category1)
        fc2.save()
        fc3 = Food_category(food=food3, category=category1)
        fc3.save()
        fc4 = Food_category(food=food4, category=category2)
        fc4.save()

    def test_substitutes_are_from_same_category(self):
        substitutes = find_substitute('poulet')
        category_research = Category.objects.filter(food_category__food__name__icontains='poulet')
        for item in substitutes:
            category_substitute = Category.objects.filter(food_category__food__name=item)
            self.assertEqual(category_substitute[0], category_research[0])

    def test_if_no_substitute_return_nothing(self):
        substitutes = find_substitute('cacao')
        self.assertEqual(substitutes, [])

    # verifier que les nutriscores sont dans l'ordre
        

