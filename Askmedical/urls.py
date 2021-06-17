from django.urls import path
from . import views
from .views import MainpageView
from .views import post_search, Tagfeature, detailpage
urlpatterns=[
    path('', post_search, name='post_search'),
    path('search/', post_search, name='post_search'),
    path('detailpage/<int:PM_id>', views.detailpage, name='detailpage'),
    path('tagpage/', Tagfeature, name='tagpage'),
]