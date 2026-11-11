from django.db import models



# cmnds
# # PS D:\dijango\myproject> python manage.py shell 
# # 13 objects imported automatically (use -v 2 for details).

# Python 3.13.15 (tags/v3.13.15:4061bc4, Aug  5 2026, 13:05:39) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# (InteractiveConsole)
# >>> from my.app.models import Emp 
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# ModuleNotFoundError: No module named 'my'
# >>> from myapp.models import Emp  
# >>> e=Emp.objects.get(pk=2)
# >>> e.salry = 600000
# >>> e.save()
# >>> e.age=23                      
# >>> e.delet()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# AttributeError: 'Emp' object has no attribute 'delet'. Did you mean: 'delete'?
# >>> e.delete()
# (1, {'myapp.Emp': 1})
# >>> e=Emp.objects.get(pk=1)
# >>> e.age=32               
# >>> e.drop()

# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# >>> Emp.objects.create(firstname='chandu',lastname='ck',salry=4300000,age=24)
# <Emp: Emp object (3)>
# # >>> 
# dijango\myproject> python manage.py createsuperuser
# Username (leave blank to use 'hp'): girichandu125
# Email address: girichandu29@gmail.com
# Password: 
# Password (again): 
# Superuser created successfully.
# PS D:\dijango\myproject> 









# Create your models here.
class Emp(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    salry = models.IntegerField()
    age = models.IntegerField()
    def __str__(self):
        return self.firstname

class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13)
    pages = models.IntegerField()
    cover_image = models.ImageField(upload_to='book_covers/')
    language = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    post = models.CharField(max_length=1000)
    thumbnail = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title