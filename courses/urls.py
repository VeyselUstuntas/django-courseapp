from django.urls import path
from courses import views

urlpatterns = [
    path("",views.index),
    path("<slug:slug>",views.courseDetail,name="course_detail"),
    path("category/<int:category_id>",views.getCoursesByCategoryId),
    path("category/<str:category_name>",views.getCoursesByCategoryName, name="courses_by_category"),

]
        