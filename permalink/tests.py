from django.test import SimpleTestCase
from django.urls import reverse, resolve, re_path, include
import permalink.views as views


class UrlsTestCase(SimpleTestCase):
    def assertUrlResolves(self, url):
        resolver_match = resolve(url)

        self.assertEqual(views.redirectPermanent, resolver_match.func)

    def test_small_l_url_resolves(self):
        self.assertUrlResolves("/l/of24/")

    def test_capital_L_url_resolves(self):
        self.assertUrlResolves("/L/of24/")

    def test_link_url_resolves(self):
        self.assertUrlResolves("/link/of24/")

    def test_small_s_url_resolves(self):
        self.assertUrlResolves("/link/of24/")
