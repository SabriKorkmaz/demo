from django.urls import path
from . import views
from .views import post_search, Tagfeature
urlpatterns=[
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', post_search, name='post_search'),
    path('search/', post_search, name='post_search'),
    path('detailpage/<int:articleid>', views.detailpage, name='detailpage'),
    path('tagpage/<int:articleid>', Tagfeature, name='tagpage'),

]
