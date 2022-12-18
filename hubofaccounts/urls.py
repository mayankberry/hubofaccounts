from django.contrib import admin
from django.urls import path
from hubofaccounts import views 


urlpatterns = [
    path("", views.index, name='hubofaccounts'),
    path("about", views.about, name='about'),
    path("scholars", views.scholars, name='scholars'),
    path("reviews", views.reviews, name='reviews'),
    path("contact", views.Contact, name='Contact'),
    path("myspace", views.myspace, name='myspace'),
    path("handlelogin", views.handlelogin, name='handlelogin'),
    path("upload", views.upload, name="upload"),
]