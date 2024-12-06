from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('reports/', views.reports, name='reports'),
    # path('services/', views.services, name="services"),
    path('careers/', views.careers, name="careers"),

    path('add_school/', views.add_school, name="add_school"),
    path("list-schools/", views.list_schools, name="list_schools"),
]
