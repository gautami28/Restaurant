from django.contrib import admin
from . models import Category, Post,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class MealsAdmin(SummernoteModelAdmin): # instead of ModelAdmin
    summernote_fields = '__all__'
    search_fields = ['title']

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)


