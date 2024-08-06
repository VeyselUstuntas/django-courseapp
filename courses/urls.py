from django.urls import path
#from courses.views import home, kurslar   ya da
from . import views

urlpatterns = [
    path('',views.home),
    path('index',views.home),
    path("kurslar",views.kurslar),
]
