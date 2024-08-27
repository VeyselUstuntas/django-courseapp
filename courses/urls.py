from django.urls import path
from courses import views
urlpatterns = [
    path("",views.index,name="courses"),
    path("<slug:slug>",views.courseDetail,name="course_detail"),
    path("category/<slug:slug>",views.getCoursesByCategoryName, name="courses_by_category"),
]
        