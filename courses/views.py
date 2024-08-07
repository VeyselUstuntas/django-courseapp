from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render

data = {
    "programming": "programlama Kategorisine ait Kurslar",
    "web-development": "Web Geliştirme Kategorisine Ait Kurslar",
    "mobile":"Mobil kategorisine Ait Kurslar",
}


def coursesList(request):
    return HttpResponse("Courses List")

def courseDetail(request,course_name):
    return HttpResponse(f"{course_name} Course Details")


def getCoursesByCategoryName(request,category_name):
    try:
        text = data[category_name]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Yanlış Kategori Seçimi")


def getCoursesByCategoryId(request, category_id):
    category_list = list(data.keys())

    if category_id > len(category_list) or category_id == 0:
        return HttpResponseNotFound("Hatalı Kategori...")
    else:
        redirect_text = category_list[category_id - 1]
        return HttpResponseRedirect(f'/course/category/{redirect_text}')


