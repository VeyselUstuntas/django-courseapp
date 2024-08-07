from django.urls import path

from pages import views


urlpatterns = [
    path('',views.home),
    path('home',views.home),
    path("communication",views.communitacion),
    path("about-us",views.aboutUs),
]
