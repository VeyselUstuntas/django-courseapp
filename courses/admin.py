from django.contrib import admin
from courses.models import Course,Category

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","date","isActive","slug",)
    list_display_links = ("title","slug",)
    readonly_fields = ("slug",)
    list_filter = ("title","isActive",)
    list_editable = ("isActive","date",)
    search_fields = ("title","description",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass    
