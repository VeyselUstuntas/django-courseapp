from django.urls import path

from pages import views


urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path("contact",views.contact,name="contact"),
    path("about",views.about,name="about"),
]
