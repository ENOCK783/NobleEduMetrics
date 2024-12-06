from django.shortcuts import render, redirect, get_object_or_404
from .models import County, School
from .forms import SchoolForm

# Home View
def home(request):
    return render(request, 'home.html')

# About View
def about(request):
    return render(request, 'about.html')

# Services View
def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')

# Careers View
def careers(request):
    return render(request, 'careers.html')

# Reports View
def reports(request):
    return render(request, 'reports.html')

def add_school(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_schools")
    else:
        form = SchoolForm()
    return render(request, "add_school.html", {"form": form})

def list_schools(request):
    counties = County.objects.all()
    return render(request, "list_schools.html", {"counties": counties})