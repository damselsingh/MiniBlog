from django.contrib import admin
from .models import post, comment
# Register your models here.
@admin.register(post)

class postModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'date', 'user']

@admin.register(comment)

class postModelAdmin(admin.ModelAdmin):
    list_display = ['posts', 'user', 'content']