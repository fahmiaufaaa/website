from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('trending/',views.trending, name='trending'),
    path('sport/',views.sport, name='sport'),
    path('politics/',views.politics, name='politics'),
    path('lifestyle/',views.lifestyle, name='lifestyle'),
    path('entertainment/',views.entertainment, name='entertainment'),
    path('healty/',views.healty, name='healty'),
]