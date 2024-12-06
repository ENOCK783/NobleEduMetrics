from django.contrib import admin
from .models import County, School

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Customize fields shown in the admin list view

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'county', 'num_teachers', 'num_learners', 'has_electricity', 'has_infrastructure')
    list_filter = ('county', 'has_electricity', 'has_infrastructure')  # Add filters
    search_fields = ('name',)  # Add a search bar for schools

