# awesome_website/urls.py

from django import views
from django.conf.urls import include, url
from django.contrib import admin
from users import views

urlpatterns = [
    url(r"^", include("users.urls")),
    url(r"^admin/", admin.site.urls),
    url("", views.dashboard, name='dashboard')
]