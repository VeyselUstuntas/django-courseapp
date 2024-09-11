from datetime import datetime
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.core.paginator import Paginator

from courses.models import Category, Course

def index(request):
    courses = Course.objects.filter(isActive=1,isHome=True).order_by("date")
    category = Category.objects.all()

    return render(request, "courses/index.html",{
        "courses":courses,
        "categories":category
    })

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        courses = Course.objects.filter(isActive=True,title__contains=q).order_by("date")
        categories = Category.objects.all()
    else:
        return redirect("/courses")

    return render(request, "courses/search.html",{
        "courses":courses,
        "categories":categories,
    })
    

def courseDetail(request,slug):
    course = get_object_or_404(Course,slug=slug)
    context = {
        "course":course,
    }
    return render(request, "courses/course_details.html",context)


def getCoursesByCategoryName(request,slug):
    courses = Course.objects.filter(isActive=True, categories__slug = slug).order_by("date")
    category = Category.objects.all()

    paginator = Paginator(courses,3) # her sayfada 1 tane kurs gözüksün
    page = request.GET.get('page',1)

    page_obj = paginator.page(page)

    print(paginator.page_range)
    print("bu kadar sayfaya sığdı ", paginator.num_pages)# kaç sayfaya sığdı
    print("kaç tane kurs kaydı var ", paginator.count) #kaç sayfa olduğunu söyler
    
    
    return render(request, "courses/list.html",{
        "page_obj":page_obj,
        "categories":category,
        "selected_category":slug
    })


def createCourse(request):
    if request.method == "POSt":
        pass
    else:
        return render(request,"courses/create-course.html")



