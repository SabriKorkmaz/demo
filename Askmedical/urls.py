from django.urls import path
from . import views
from .views import MainpageView
from .views import post_search
urlpatterns=[
    path('', post_search, name='post_search'),
    path('search/', post_search, name='post_search'),
]
