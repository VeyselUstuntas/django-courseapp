from datetime import datetime
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from courses.models import Category, Course

def index(request):
    courses = Course.objects.filter(isActive=1)
    category = Category.objects.all()

    return render(request, "courses/index.html",{
        "courses":courses,
        "categories":category
    })


def courseDetail(request,slug):
    course = get_object_or_404(Course,slug=slug)
    context = {
        "course":course,
    }
    return render(request, "courses/course_details.html",context)


def getCoursesByCategoryName(request,slug):
    courses = Course.objects.filter(category__slug = slug,isActive = True)
    category = Category.objects.all()

    return render(request, "courses/index.html",{
        "courses":courses,
        "categories":category,
        "selected_category":slug
    })




