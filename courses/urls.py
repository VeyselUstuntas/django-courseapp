from django.urls import path
#from courses.views import home, kurslar   ya da
from courses import views

urlpatterns = [
    path("",views.coursesList),
    path("courses-list",views.coursesList),
    path("<course_name>",views.courseDetail),
    path("category/<int:category_id>",views.getCoursesByCategoryId),
    path("category/<str:category_name>",views.getCoursesByCategoryName),

]
        