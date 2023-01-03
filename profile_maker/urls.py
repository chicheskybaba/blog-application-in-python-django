from django.urls import path
from . import views
from django_project import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create/', views.create_profile, name = 'create'),
]

