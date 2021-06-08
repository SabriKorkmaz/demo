from django.urls import path
from . import views
from .views import MainpageView
from .views import post_search
urlpatterns=[
    path('', MainpageView.as_view(), name='Mainpage'),
    path('search/', post_search, name='post_search'),
]
