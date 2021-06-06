from django.urls import path
from .views import MainpageView
from .views import SearchView
from .views import index
urlpatterns=[
    path('', MainpageView.as_view(), name='Mainpage'),
    path('search/', SearchView.as_view(), name='Search'),
    path('results/',index,name="index"),
]