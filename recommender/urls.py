# courses/urls.py
from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path('', index, name='home'),  # This maps the root URL to the 'index' view

    path('api/course-recommendation/', views.course_recommendation, name='course_recommendation'),
]
