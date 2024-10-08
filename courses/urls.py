from django.urls import path
from courses import views
urlpatterns = [
    path("",views.index,name="courses"),
    path("search",views.search, name = "search"),
    path("course-list",views.courseList, name="course_list"),
    path("course-edit/<int:id>",views.courseEdit, name="course_edit"),
    path("course-delete/<int:id>",views.courseDelete, name="course_delete"),
    path("create-course",views.createCourse,name="create_course"),
    path("upload",views.upload, name="upload_image"),
    path("<slug:slug>",views.courseDetail,name="course_detail"),
    path("category/<slug:slug>",views.getCoursesByCategoryName, name="courses_by_category"),
]
        