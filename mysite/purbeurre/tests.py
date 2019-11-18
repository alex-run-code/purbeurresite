from django.test import TestCase
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse
from django.test.utils import override_settings


class CustomUserCreationFormTest(TestCase):

    def test_empty_email_return_error(self):
        """
        If the user inputs an empty mail, the page
        should return an error
        """
        form = CustomUserCreationForm(data={'email': '', 'first_name': 'Thomas'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ["This field is required."])

    def test_empty_first_name_return_error(self):
        """
        If the user leave the name field empty, the page
        should return an error
        """
        form = CustomUserCreationForm(data={'email': 'francois@gmail.com', 'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'], ["This field is required."])

    def test_existing_email_return_error(self):
        """
        If the user inputs an email address already used,
        the page should return an error
        """
        user = CustomUser(email='francois@gmail.com', first_name='francois', password='147www258Ab')
        user.save()
        form = CustomUserCreationForm(data={'email': 'francois@gmail.com', 'first_name': 'francois'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ["User with this Email address already exists."])

    def test_wrong_email_return_error(self):
        """
        If the user inputs an incorrect email address,
        the page should return an error
        """
        user = CustomUser(email='francois@gmail.com', first_name='francois', password='147www258Ab')
        user.save()
        form = CustomUserCreationForm(data={'email': 'francoisgmailcom', 'first_name': 'francois'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ["Enter a valid email address."])

    def test_user_is_created_after_submitting_form(self):
        """
        If the user inputs the right informations,
        the account is created in the database
        """
        self.client.post(reverse('purbeurre:signup'), {'email': 'francois@gmail.com', 'first_name': 'francois', 'password1': '147www258Ab', 'password2': '147www258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francois@gmail.com').count(), 1)

    @override_settings(DEBUG=True)
    def test_user_is_not_created_after_submitting_wrong_mail(self):
        """
        If the user inputs a wrong email, 
        the account is not created in the database
        """
        self.client.post(reverse('purbeurre:signup'), {'email': 'francoisgmail.com', 'first_name': 'francois', 'password1': '147www258Ab', 'password2': '147www258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francoisgmail.com').count(), 0)

    @override_settings(DEBUG=True)
    def test_user_is_not_created_after_submitting_no_name(self):
        """
        If the user doesnt input a name, 
        the account is not created in the database
        """
        self.client.post(reverse('purbeurre:signup'), {'email': 'francois@gmail.com', 'first_name': '', 'password1': '147www258Ab', 'password2': '147www258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francois@gmail.com').count(), 0)

    @override_settings(DEBUG=True)
    def test_user_is_not_created_after_submitting_wrong_password2(self):
        """
        If the user input an incorrect confirmation password,
        the account is not created in the database
        """
        self.client.post(reverse('purbeurre:signup'), {'email': 'francois@gmail.com', 'first_name': 'francois', 'password1': '147www258Ab', 'password2': '147ww258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francois@gmail.com').count(), 0)
