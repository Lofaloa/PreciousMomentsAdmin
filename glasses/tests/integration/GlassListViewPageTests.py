from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


from glasses.models import Glass

class GlassDetailTests(StaticLiveServerTestCase):

    def testExample(self):
        self.assertTrue(False)