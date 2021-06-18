from django.test import SimpleTestCase
from django.urls import resolve, reverse
from Askmedical.views import registerPage, loginPage, logoutUser, Tagfeature, post_search, detailpage
from django.test import TestCase, Client
from Askmedical.models import Article, Tag
import json

#classes are inherited from SimpleTestCase here
# I am testing the urls of Askmedical website to see if
#Django looks at the files which Starts with Test, also looks at the classes which starts with Test

# Here I will test each url if they are set to correct views
class TestUrlsAskmedical(SimpleTestCase):

    def test_register_url_isresolved(self):
        #lets see when I resolve the register url, if it will be set to my registerPage view
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerPage) #resulted successfully.

    def test_login_url_isresolved(self):
        #lets see when I resolve the login url, if it will be set to my loginPage view
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage) #resulted successfully.

    def test_logout_url_isresolved(self):
        #lets see when I resolve the logout url, if it will be set to my logoutUser view
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser) #resulted successfully.

    def test_search_url_isresolved(self):
        # lets see when I resolve the search url, if it will be set to my post_search view
        url = reverse('post_search')
        self.assertEquals(resolve(url).func, post_search)  # resulted successfully.

    def test_detailpage_url_isresolved(self):
        # lets see when I resolve the detailpage url(shows article details), if it will be set to my detailpage view
        url = reverse('detailpage', args=[2]) #it expects the article id to complete the url
        self.assertEquals(resolve(url).func, detailpage)  # resulted successfully.

    def test_tagpage_url_isresolved(self):
        # lets see when I resolve the tagpage url(which is used for tag insertion), if it will be set to my TagFeature view
        url = reverse('tagpage', args=[2]) #it expects the article id to complete the url
        self.assertEquals(resolve(url).func, Tagfeature)  # resulted successfully.


# class TestAskmedicalViews(TestCase):
#
#         def SetEnvUp(self):
#             self.client = Client()
#             self.post_url = reverse('post_search')
#             self.detail_url = reverse('detailpage', args=[2])
#
#         # I will test here if the post search view work properly and response search.html
#         def test_post_search_GET(self):
#             response = self.client.get(self.post_url)
#             print(self.post_url)
#             self.assertEquals(response.status_code, 200)
#             #self.assertTemplateUsed(response, 'search.html')

        # def test_detailpage_POST(self):
        #     response = self.client.post(self.detail_url)
        #
        #     self.assertEquals(response.status_code, 200)
        #     self.assertTemplateUsed(response, 'search.html')