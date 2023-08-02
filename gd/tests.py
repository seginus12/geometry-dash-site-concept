from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib import admin

class QuestionModelTests(TestCase):

    def test(self):
        # some tests
        self.assertIs(False, True)
