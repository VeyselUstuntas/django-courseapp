from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programming": "programlama Kategorisine ait Kurslar",
    "web-development": "Web Geliştirme Kategorisine Ait Kurslar",
    "mobile":"Mobil kategorisine Ait Kurslar",
    "devops":"Azure Bulut Bilişim Hizmetleri",
}

def index(request):
    category_list = list(data.keys())


    return render(request, "courses/index.html",{
        "categories":category_list
    })


def courseDetail(request,course_name):
    return HttpResponse(f"{course_name} Course Details")


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


