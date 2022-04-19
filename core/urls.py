from django.urls import path
from .views import views

urlpatterns = [
    path(views[i].path, views[i].as_view(), name=f"core_{i}") for i in views
]