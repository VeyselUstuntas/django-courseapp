from datetime import datetime
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from courses.models import Category, Course

data = {
    "programming": "programlama Kategorisine ait Kurslar",
    "web-development": "Web Geliştirme Kategorisine Ait Kurslar",
    "mobile":"Mobil kategorisine Ait Kurslar",
    "devops":"Azure Bulut Bilişim Hizmetleri",
}



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


def getCoursesByCategoryName(request,category_name):
    try:
        text = data[category_name]
        return render(request, "courses/courses_list.html", {
            "category": category_name,
            "category_info":text
        })
    except:
        return HttpResponseNotFound("Yanlış Kategori Seçimi")


def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())

    if category_id > len(category_list) or category_id == 0:
        return HttpResponseNotFound("Hatalı Kategori...")
    else:
        category_name = category_list[category_id - 1]

        redirect_url = reverse("courses_by_category",args=[category_name])

        return redirect(redirect_url)


