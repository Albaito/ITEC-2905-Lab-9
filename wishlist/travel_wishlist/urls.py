''' File is for web app routing '''

from django.urls import path
from . import views

urlpatterns =[
    # path syntax: path('[url ender]', views.[views.py function], name=[''name for url])
    path('', views.place_list, name='place_list'),
    path('visited', views.places_visited, name='places_visited'),
    path('place/<int:place_pk>/was_visited/', views.place_was_visited, name='place_was_visited'),
    path('place/<int:place_pk>', views.place_details, name='place_details')

]