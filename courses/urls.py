from django.urls import path
#from courses.views import home, kurslar   ya da
from courses import views

urlpatterns = [
    path("",views.index),
    path("<course_id>",views.courseDetail,name="course_detail"),
    path("category/<int:category_id>",views.getCoursesByCategoryId),
    path("category/<str:category_name>",views.getCoursesByCategoryName, name="courses_by_category"),

]
        