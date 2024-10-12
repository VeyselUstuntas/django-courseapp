from datetime import datetime
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required,user_passes_test

from courses.forms import CourseCreateForm, CourseEditForm, UploadForm
from courses.models import Category, Course, UploadModel

import random

def index(request):
    courses = Course.objects.filter(isActive=1,isHome=True).order_by("date")
    category = Category.objects.all()

    return render(request, "courses/index.html",{
        "courses":courses,
        "categories":category
    })


def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def createCourse(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect("courses")
    else:
        form = CourseCreateForm()
    return render(request,"courses/create-course.html",{"form":form})


@user_passes_test(isAdmin)
def courseList(request):
    courses = Course.objects.all()
    return render(request,"courses/course-list.html",{
        "courses":courses,
    })


def courseEdit(request,slug):
    course = Course.objects.get(slug=slug)
    if request.method == "POST":
        form = CourseEditForm(request.POST,request.FILES, instance=course)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseEditForm(instance=course)
    return render(request,"courses/edit-course.html",{"course":course,"form":form})


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

    paginator = Paginator(courses,3) # her sayfada 3 tane kurs gözüksün
    page = request.GET.get('page',1)

    page_obj = paginator.page(page)

    print(paginator.page_range)
    print("bu kadar sayfaya sığdı ", paginator.num_pages)# kaç sayfaya sığdı
    print("kaç tane kurs kaydı var ", paginator.count) #kaç sayfa olduğunu söyler
    print(page_obj.number)
    
    
    return render(request, "courses/list.html",{
        "page_obj":page_obj,
        "categories":category,
        "selected_category":slug
    })








def courseDelete(request, slug):
    course = get_object_or_404(Course,slug=slug)

    if request.method == "POST":
        Course.delete(course)
        return redirect("course_list")
    else:
        return render(request,"courses/course-delete.html",{"course":course})
    

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            model = UploadModel(image= request.FILES["image"])
            print(model.image)
            model.save()
            return render(request,"courses/success.html")
    else:
        form = UploadForm()
    return render(request, "courses/upload.html",{"form":form})
