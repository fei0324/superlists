from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):

	def test_root_url_resolves_to_home_page_view(self):
		found = resolve('/')
		# resolve() has the attribute func:
		# The view function that would be used to serve the URL
		self.assertEqual(found.func, home_page)