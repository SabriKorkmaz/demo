from django.test import SimpleTestCase
from django.urls import resolve, reverse
from Askmedical.views import registerPage, loginPage, logoutUser, Tagfeature, post_search, detailpage
from django.test import TestCase, Client
from Askmedical.models import Article, Tag
from django.utils import timezone
import json

#classes are inherited from SimpleTestCase here
# I am testing the urls of Askmedical website to see if
#Django looks at the files which Starts with Test, also looks at the classes which starts with Test

# Here I will test each url if they are set to correct views
class TestUrlsAskmedical(SimpleTestCase):

    def test_register_url_isresolved(self):
        #lets see when I resolve the register url, if it will be set to my registerPage view
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerPage) #Case1-resulted successfully.

    def test_login_url_isresolved(self):
        #lets see when I resolve the login url, if it will be set to my loginPage view
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage) #Case2-resulted successfully.

    def test_logout_url_isresolved(self):
        #lets see when I resolve the logout url, if it will be set to my logoutUser view
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser) #Case3-resulted successfully.

    def test_search_url_isresolved(self):
        # lets see when I resolve the search url, if it will be set to my post_search view
        url = reverse('post_search')
        self.assertEquals(resolve(url).func, post_search)  #Case4-resulted successfully.

    def test_detailpage_url_isresolved(self):
        # lets see when I resolve the detailpage url(shows article details), if it will be set to my detailpage view
        url = reverse('detailpage', args=[2]) #it expects the article id to complete the url
        self.assertEquals(resolve(url).func, detailpage)  #Case5-resulted successfully.

    def test_tagpage_url_isresolved(self):
        # lets see when I resolve the tagpage url(which is used for tag insertion), if it will be set to my TagFeature view
        url = reverse('tagpage', args=[2]) #it expects the article id to complete the url
        self.assertEquals(resolve(url).func, Tagfeature)  #Case6- resulted successfully.


class TestAskmedicalViews(TestCase):


        # I will test here if the post search view work properly and response search.html
        def test_post_search_GET(self):
            client = Client()

            response = client.get(reverse('post_search'))

            self.assertEquals(response.status_code, 302) #Case7- resulted successfully.


        def test_detailpage_GET(self):
            client = Client()

            response = client.get(reverse('detailpage', args=[2]))

            self.assertEquals(response.status_code, 302) #Case8- resulted successfully.

        def test_tagpage_GET(self):
            client = Client()

            response = client.get(reverse('tagpage', args=[2]))

            self.assertEquals(response.status_code, 302) #Case9- resulted successfully.

class TestAskmedicalModels(TestCase):

    def setUpArticleModel(self):
        self.article1 = Article.objects.create(

        abstract = 'article1',
        PM_id = '123234',
        title = 'influenza effect',
        keywords = 'health, influenze',
        authors = 'suzan uskudarli',
        publication_date =timezone.now(),
        )
        return self.article1

    def test_if_article_is_instance(self):
        article = self.setUpArticleModel()
        self.assertTrue(isinstance(article, Article)) #Case10- resulted successfully.

    def test_if_article_is_created(self):
        #Here I will test if the Article model is created as I build with the required fields
        # which is equal to ones that I input
        article = self.setUpArticleModel()
        check_article_fields = Article.objects.filter(PM_id='123234').values()
        #print(check_article_fields[0].get('authors'))
        self.assertEqual(check_article_fields[0].get('authors'), 'suzan uskudarli') #Case11- resulted successfully.
        self.assertEqual(check_article_fields[0].get('title'), 'influenza effect') #Case12- resulted successfully.