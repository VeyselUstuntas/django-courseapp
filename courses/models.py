from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(null=False,default="",unique=True, db_index=True,blank=True,editable=True)
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.name}"
    
class Course(models.Model):
    title = models.CharField(max_length=50)
    description =models.TextField()
    image = models.ImageField(upload_to="images",default="")   
    date = models.DateField(auto_now_add=True)
    isActive = models.BooleanField(default=False)
    isHome = models.BooleanField(default=False)
    slug = models.SlugField(null=False,default="",unique=True, db_index=True,blank=True,editable=False)
    categories = models.ManyToManyField(Category,related_name="kurslar",blank=True)
   
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)


    def __str__(self):
        return f"{self.title}"


class UploadModel(models.Model):
    image = models.ImageField(upload_to="images")
