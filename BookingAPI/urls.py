from django.urls import path
from . import views

urlpatterns = [
    path('comments', views.form_view),
]
