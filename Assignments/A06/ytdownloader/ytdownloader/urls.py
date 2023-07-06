from django.contrib import admin
from django.urls import path
from ytapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("search_endpoint", views.getstreams, name="search_endpoint"),
    path("add_download", views.start_download, name="add_download"),
]
