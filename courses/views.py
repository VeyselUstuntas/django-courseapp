from datetime import date
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programming": "programlama Kategorisine ait Kurslar",
    "web-development": "Web Geliştirme Kategorisine Ait Kurslar",
    "mobile":"Mobil kategorisine Ait Kurslar",
    "devops":"Azure Bulut Bilişim Hizmetleri",
}

db = {
    "courses" : [
        {
            "title": "JavaScript Kursu",
            "description": "JavaScript Kursu Açıklaması",
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/1662526_fc1c_3.jpg",
            "slug":"javascript-kursu",
            "date": date(2024,7,19),
            "is-active" : True,
        },
        {
            "title": "Python Kursu",
            "description": "Python Kursu Açıklaması",
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/2463492_8344_3.jpg",
            "slug":"python-kursu",
            "date": date(2024,5,5),
            "is-active" : False,

        },
        {
            "title": "Web Geliştirme Kursu",
            "description": "Web Geliştirme Kursu Açıklaması",
            "imageUrl":"https://img-c.udemycdn.com/course/750x422/1258436_2dc3_4.jpg",
            "slug":"web-gelistirme-kursu",
            "date": date(2024,12,22),
            "is-active" : True,

        }
    ],

    "categories":[
        {"id":1, "name":"Programlama","slug":"programlama"},
        {"id":2, "name":"Web Gelişirme","slug":"web-gelistirme"},
        {"id":3, "name":"Mobil Uygulamalar","slug":"mobil-uygulamalar"},
        {"id":4, "name":"Bulut Hizmetleri","slug":"bulut-hizmetleri"},
    ]
}

def index(request):
    courses = db["courses"]
    category = db["categories"]

    return render(request, "courses/index.html",{
        "courses_list":courses,
        "categories":category
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


