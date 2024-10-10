from django import forms

from courses.models import Course


# SADE FORM CLASS OLUŞTURMA

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
    


    #### MODELLER İLE FORM CLASS OLUŞTURMA

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["title","description","image"]
        labels = {
            "title":"Kurs Başlığı:",
            "description":"Kurs Açıklaması:",
            "image":"Kurs Görseli:",
        }
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
        }
        error_messages = {
            "title":{"required":"Kurs Başlığını Giriniz!", "max_length":"Geçtin sınırı"},
            "description":{"required":"Kurs Açıklamasını Giriniz!"},
            "image":{"required":"Kurs Görselini Seçiniz!"}

        }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        labels = {
            "title":"Kurs Başlığı:",
            "description":"Kurs Açıklaması:",
            "image":"Kurs Görseli:",
            "isActive":"Aktif Mi?",
            "isHome":"Ana Sayfada Mı?",
            "categories":"Kurs Katgorisi"
        }
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "isActive":forms.CheckboxInput(),
            "isHome":forms.CheckboxInput(),
            "categories":forms.SelectMultiple(attrs={"class":"form-control"}),
        }
        error_messages = {
            "title":{"required":"Kurs Başlığını Giriniz!", "max_length":"Geçtin sınırı"},
            "description":{"required":"Kurs Açıklamasını Giriniz!"},
            "image":{"required":"Kurs Görselini Seçiniz!"}

        }


class UploadForm(forms.Form):
    image = forms.FileField(
        label="Kurs Görseli",
        widget=forms.FileInput(attrs={"class":"form-control"}),
        error_messages={"required":"Lütfen Bir Medya Yükleyin"},
    )
