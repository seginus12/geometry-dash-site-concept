from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib import admin

class QuestionModelTests(TestCase):

    def amdin_is_created(self):
        User = get_user_model()
        superusers = User.objects.filter(is_superuser=True)
        print(superusers)
        self.assertIs(superusers, True)
