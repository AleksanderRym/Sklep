from django.contrib import admin
from django.urls import path, include
from Gry.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('gatunek/<id>/', gatunek, name='gatunek'),
    path('gra/<id>/',gra, name='gra'),
    path('search', gra_nazwa, name='search'),
    path('login', loginPage, name='login'),
    path('register', registerPage, name='register'),
    path('logout', logoutUser, name='logout'),

]
