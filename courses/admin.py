from django.contrib import admin
from courses.models import Course,Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","date","isActive","isHome","slug","category_list",)
    list_display_links = ("title","slug",)
    readonly_fields = ("slug",)
    list_filter = ("title","isActive","isHome","categories",)
    list_editable = ("isActive","isHome")
    search_fields = ("title","description","category")


    def category_list(self,course_obj):
        html=""
        for category in course_obj.categories.all():
            html += category.name + ", "

        return html 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug","course_count",)
    prepopulated_fields = {"slug":("name",),}
    list_filter = ("name",)


    def course_count(self, category_obj):
        return category_obj.kurslar.count()
    

