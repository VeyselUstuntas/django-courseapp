from django import forms

from courses.models import Course


# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label = "Course Title", 
#         error_messages={"required":"Kurs Başlığı Girilmelidir"},
#         widget=forms.TextInput(attrs={"class":"form-control"}),
#         )

#     description = forms.CharField(
#         label="Description",
#         widget=forms.Textarea(attrs={"class":"form-control"}),
#         error_messages={"required":"Kurs Açıklaması Girilmelidir"},

#         )

#     imageUrl = forms.CharField(
#         label = "Course Image", # bu özellik html sayfasında ezildi
#         widget=forms.TextInput(attrs={"class":"form-control"}),
#         error_messages={"required":"Kurs Görseli Girilmelidir"},

#         )
    

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title","description","imageUrl"]
        labels = {
            "title":"Kurs Başlığı:",
            "description":"Kurs Açıklaması:",
            "imageUrl":"Kurs Görseli:",
        }
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "imageUrl":forms.TextInput(attrs={"class":"form-control"})
        }
        error_messages = {
            "title":{"required":"Kurs Başlığını Giriniz!", "max_length":"Geçtin sınırı"},
            "description":{"required":"Kurs Açıklamasını Giriniz!"},
            "imageUrl":{"required":"Kurs Görselini Seçiniz!"}

        }
