from django.contrib import admin
from .models import Category, Post
from .models import Message


admin.site.register(Message)
admin.site.register(Category)
admin.site.register(Post)


# Register your models here.
