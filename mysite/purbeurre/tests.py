# ajout à la base de donnée
# l'utilisateur a bien été créé                 x
# l'utilisateur a été créé avec le bon email    x
# l'utilisateur a été créé avec le bon nom      x

# erreurs
# si le champ email est vide, affiche une erreur                        x
# si le champ first_name est vide, affiche une erreur                   x
# si l'email est déjà utilisée, affiche une erreur                      x
# si l'adresse email n'est pas au bon format, affiche une erreur
# si le mot de passe ne contient que des chiffres, affiche une erreur
# si le mot de passe est trop court, affiche une erreur
# si le mot de passe est trop simple, affiche une erreur

# utilisation
# si l'utilisateur est connecté, le bouton de login affiche "mon compte"
# si l'utilisateur est connecté et qu'il clique sur "mon compte", ca affiche la page de son compte
# si l'utilisateur est connecté et qu'il clique sur "déconnexion", ca le déconnecte
# si l'utilisateur n'est pas connecté, le bouton de login affiche "se connecter"

from django.test import TestCase
from .models import CustomUserManager, CustomUser
from .forms import ItemForm, CustomUserCreationForm
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm

class CustomUserCreationFormTest(TestCase):

    def test_empty_email_return_error(self):
        form = CustomUserCreationForm(data={'email':'','first_name':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],["This field is required."])

    def test_empty_first_name_return_error(self):
        form = CustomUserCreationForm(data={'email':'','first_name':''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'],["This field is required."])

    def test_existing_email_return_error(self):
        user = CustomUser(email='francois@gmail.com',first_name='francois',password='147www258Ab')
        user.save()
        form = CustomUserCreationForm(data={'email':'francois@gmail.com','first_name':'francois'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],["User with this Email address already exists."])

    def test_wrong_email_return_error(self):
        user = CustomUser(email='francois@gmail.com',first_name='francois',password='147www258Ab')
        user.save()
        form = CustomUserCreationForm(data={'email':'francoisgmailcom','first_name':'francois'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],["Enter a valid email address."])

    def test_user_is_created_after_submitting_form(self):
        self.client.post(reverse('purbeurre:signup'), {'email':'francois@gmail.com', 'first_name':'francois', 'password1':'147www258Ab', 'password2':'147www258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francois@gmail.com').count(), 1)

    def test_user_is_not_created_after_submitting_wrong_mail(self):
        self.client.post(reverse('purbeurre:signup'), {'email':'francoisgmail.com', 'first_name':'francois', 'password1':'147www258Ab', 'password2':'147www258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francoisgmail.com').count(), 0)

    def test_user_is_not_created_after_submitting_no_name(self):
        self.client.post(reverse('purbeurre:signup'), {'email':'francois@gmail.com', 'first_name':'', 'password1':'147www258Ab', 'password2':'147www258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francois@gmail.com').count(), 0)

    def test_user_is_not_created_after_submitting_wrong_password2(self):
        self.client.post(reverse('purbeurre:signup'), {'email':'francois@gmail.com', 'first_name':'francois', 'password1':'147www258Ab', 'password2':'147ww258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francois@gmail.com').count(), 0)

    # trying to test that user is logged, but it doesnt work
    def test_user_is_logged_in_after_logging_in(self):
        self.client.post(reverse('login'), {'username':'cambefort.alex@gmail.com', 'password':'210991Ab'})
        self.assertEqual(user.is_authenticated(), True)


