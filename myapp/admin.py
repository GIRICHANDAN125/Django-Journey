from django.contrib import admin
from .models import Emp, Author, Book

# Register your models here.
admin.site.register(Emp)
admin.site.register(Author)
admin.site.register(Book)