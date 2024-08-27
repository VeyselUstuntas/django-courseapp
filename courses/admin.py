from django.contrib import admin
from courses.models import Course,Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","date","isActive","slug","category",)
    list_display_links = ("title","slug",)
    readonly_fields = ("slug",)
    list_filter = ("title","isActive","category",)
    list_editable = ("isActive",)
    search_fields = ("title","description","category")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug",)
    prepopulated_fields = {"slug":("name",),}
    list_filter = ("name",)

