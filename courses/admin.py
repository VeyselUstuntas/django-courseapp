from django.contrib import admin
from courses.models import Course,Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","date","isActive","isHome","slug","category_list",)
    list_display_links = ("title","slug",)
    readonly_fields = ("slug",)
    list_filter = ("title","isActive","isHome","categories",)
    list_editable = ("isActive","isHome")
    search_fields = ("title","description","categories__name")


    def category_list(self,course_obj):
        if len(course_obj.categories.all()) == 0:
            return "KURSA KATEGORİ ATANMAMIŞ"
        else:
            html=""
            for index, category in enumerate(course_obj.categories.all()):
                if index == len(course_obj.categories.all()) - 1:
                    html += category.name
                else:
                    html += category.name + ", "          
            return html 


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug","course_count","courses_under_category",)
    prepopulated_fields = {"slug":("name",),}
    list_filter = ("name",)


    def course_count(self, category_obj):
        return category_obj.kurslar.count()
    
    def courses_under_category(self,category_obj):
        html = ""
        for index, course in enumerate(category_obj.kurslar.all()):
            if index == len(category_obj.kurslar.all()) -1 :
                html += f"{index+1}-{course.title} "
            else:
                html += f"{index+1}-{course.title}, "
        return html
    

