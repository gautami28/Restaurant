from django.contrib import admin
from . models import Category, Meals
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class MealsAdmin(SummernoteModelAdmin): # instead of ModelAdmin
    summernote_fields = '__all__'

admin.site.register(Meals)
admin.site.register(Category)