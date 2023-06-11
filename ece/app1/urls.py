from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home/',views.home,name="home"),
    path("career/",views.career,name="career"),
    path("course/",views.courses,name="courses"),
    path("gadgets/",views.Gadgets,name="gadgets"),
    path("about/",views.about,name="about"),
]
