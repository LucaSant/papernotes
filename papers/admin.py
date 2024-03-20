from django.contrib import admin

# Register your models here.
from .models import Post, Task

admin.site.register(Post)
admin.site.register(Task)