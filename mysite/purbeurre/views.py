from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from fooddb.research import find_substitute
from fooddb.models import Food, Favorites
from purbeurre.models import CustomUser

# Create your views here.


def index(request):
    return render(request, 'index.html')


def test_page(request):
    return render(request, 'purbeurre/test_page.html')


def account(request):
    """
    This function shows the account page of the user, with its favorites
    """
    current_user = request.user
    foods = Food.objects.filter(favorites__user__id=current_user.id)
    fav_list = []
    for food in foods:
        fav_list.append({
            'name': food.name,
            'id': food.id,
            })
    context = {'myfavorites': fav_list}
    return render(request, 'purbeurre/account.html', context)


def creation_successful(request):
    return render(request, 'purbeurre/creation_successful.html')


def signup(request):
    """
    This function creates an account for the user.
    """
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Votre compte a bien été enregistré.')
            return redirect('purbeurre:creation_successful')

    else:
        f = CustomUserCreationForm()

    return render(request, 'purbeurre/signup.html', {'form': f})


def search_result(request):
    """
    This function send the input of the user in
    the function "find_substitute" and return a
    list of substitutes
    """
    if request.method == 'POST':

        # Check if the form is valid:
        list_of_substitute = find_substitute(request.POST['search_field'])
        sub_dic = []
        if list_of_substitute:
            for sub in list_of_substitute:
                sub_dic.append({
                    'id': sub.id,
                    'name': sub.name,
                    'nutriscore': sub.nutriscore,
                    'picture_url': sub.picture_url,
                    'off_url': sub.off_url,
                    'sugar_100g': sub.sugar_100g,
                    'salt_100g': sub.salt_100g,
                    'carbohydrates_100g': sub.carbohydrates_100g,
                    'sodium_100g': sub.sodium_100g,
                    'saturated_fat_100g': sub.saturated_fat_100g,
                    'proteins_100g': sub.proteins_100g,
                    'fat_100g': sub.fat_100g,
                    })
            context = {
                'reponse': sub_dic[:5],
                'message': ''
                }
        else:
            context = {'message': 'Aucune resultat'}
        return render(request, 'purbeurre/search_result.html', context)


def food_page(request, food_id):
    """
    This function return a page with all the informations of a given food
    """
    food = Food.objects.filter(id=food_id)[0]

    context = {
        'id': food.id,
        'name': food.name,
        'nutriscore': food.nutriscore,
        'picture_url': food.picture_url,
        'off_url': food.off_url,
        'sugar_100g': food.sugar_100g,
        'salt_100g': food.salt_100g,
        'carbohydrates_100g': food.carbohydrates_100g,
        'sodium_100g': food.sodium_100g,
        'saturated_fat_100g': food.saturated_fat_100g,
        'proteins_100g': food.proteins_100g,
        'fat_100g': food.fat_100g,
        }
    return render(request, 'purbeurre/food_page.html', context)


def add_to_favorites(request):
    """
    This function adds a food in the user's favorites list.
    """
    if request.method == 'POST':
        user = CustomUser.objects.filter(id=request.POST['user_id'])[0]
        food = Food.objects.filter(id=request.POST['food_id'])[0]
        f = Favorites(
                    user=user,
                    food=food,
                    )
        f.save()
    return render(request, 'purbeurre/fav_added.html')


def fav_added(request):
    return render(request, 'purbeurre/fav_added.html')


def legal(request):
    return render(request, 'purbeurre/legal.html')
