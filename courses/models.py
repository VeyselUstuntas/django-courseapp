from django.db import models
from django.utils.text import slugify
class Course(models.Model):
    title = models.CharField(max_length=50)
    description =models.TextField()
    imageUrl = models.CharField(max_length=50, blank=False)   
    date = models.DateField()
    isActive = models.BooleanField()
    slug = models.SlugField(null=False,default="",unique=True, db_index=True,blank=True,editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(args,kwargs)


    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"