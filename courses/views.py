from datetime import datetime
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.core.paginator import Paginator

from courses.forms import CourseCreateForm, CourseEditForm
from courses.models import Category, Course

import random

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


def createCourse(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("courses")
    else:
        form = CourseCreateForm()
    return render(request,"courses/create-course.html",{"form":form})


def courseList(request):
    courses = Course.objects.all()
    return render(request,"courses/course-list.html",{
        "courses":courses,
    })

def courseEdit(request,id):
    course = Course.objects.get(id=id)
    if request.method == "POST":
        form = CourseEditForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            return redirect("course_list")

    else:
        form = CourseEditForm(instance=course)
    return render(request,"courses/edit-course.html",{"course":course,"form":form})


def courseDelete(request, id):
    course = get_object_or_404(Course,pk=id)

    if request.method == "POST":
        Course.delete(course)
        return redirect("course_list")
    else:
        return render(request,"courses/course-delete.html",{"course":course})
    

def upload(request):
    if request.method == "POST":
        uploaded_image = request.FILES.getlist("images")
        for image in uploaded_image:
            handle_uploaded_files(image)
        return render(request,"courses/success.html")
    return render(request, "courses/upload.html")


def handle_uploaded_files(file):
    number = random.randint(1,99999)
    file_name = file.name.replace(".",f"_{number}.")
    with open("temp/" + file_name, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)