# ajout à la base de donnée
# l'utilisateur a bien été créé                 x
# l'utilisateur a été créé avec le bon email    x
# l'utilisateur a été créé avec le bon nom      x

# erreurs
# si l'email est déjà utilisée, affiche une erreur
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

class UserCreationTests(TestCase):

    def test_user_was_created_with_correct_infos(self):
        """ 
        after the user fills the user creation form correctly,
        he exists in the database with the right email and first name.
        """
        user = CustomUser(email='francois@gmail.com',first_name='francois',password='147www258Ab')
        user.save()
        self.assertIs('francois@gmail.com' in CustomUser.objects.all().values_list('email', flat=True),True)
        self.assertIs(user.email is 'francois@gmail.com',True)
        self.assertIs(user.first_name is 'francois',True)
        

         