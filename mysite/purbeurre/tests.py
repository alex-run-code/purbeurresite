from django.test import TestCase
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.urls import reverse


class CustomUserCreationFormTest(TestCase):

    def test_empty_email_return_error(self):
        form = CustomUserCreationForm(data={'email': '', 'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ["This field is required."])

    def test_empty_first_name_return_error(self):
        form = CustomUserCreationForm(data={'email': '', 'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'], ["This field is required."])

    def test_existing_email_return_error(self):
        user = CustomUser(email='francois@gmail.com', first_name='francois', password='147www258Ab')
        user.save()
        form = CustomUserCreationForm(data={'email': 'francois@gmail.com', 'first_name': 'francois'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ["User with this Email address already exists."])

    def test_wrong_email_return_error(self):
        user = CustomUser(email='francois@gmail.com', first_name='francois', password='147www258Ab')
        user.save()
        form = CustomUserCreationForm(data={'email': 'francoisgmailcom', 'first_name': 'francois'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ["Enter a valid email address."])

    def test_user_is_created_after_submitting_form(self):
        self.client.post(reverse('purbeurre:signup'), {'email': 'francois@gmail.com', 'first_name': 'francois', 'password1': '147www258Ab', 'password2': '147www258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francois@gmail.com').count(), 1)

    def test_user_is_not_created_after_submitting_wrong_mail(self):
        self.client.post(reverse('purbeurre:signup'), {'email': 'francoisgmail.com', 'first_name': 'francois', 'password1': '147www258Ab', 'password2': '147www258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francoisgmail.com').count(), 0)

    def test_user_is_not_created_after_submitting_no_name(self):
        self.client.post(reverse('purbeurre:signup'), {'email': 'francois@gmail.com', 'first_name': '', 'password1': '147www258Ab', 'password2': '147www258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francois@gmail.com').count(), 0)

    def test_user_is_not_created_after_submitting_wrong_password2(self):
        self.client.post(reverse('purbeurre:signup'), {'email': 'francois@gmail.com', 'first_name': 'francois', 'password1': '147www258Ab', 'password2': '147ww258Ab'})
        self.assertEqual(CustomUser.objects.filter(email='francois@gmail.com').count(), 0)
