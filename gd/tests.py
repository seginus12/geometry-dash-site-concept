from django.test import SimpleTestCase

class UnitTests(SimpleTestCase):
    def test(self):
        self.assertIs(False, True)
