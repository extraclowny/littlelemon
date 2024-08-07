from django.urls import path
from . import views
from .views import menuview, bookingview

urlpatterns = [
    path('comments', views.form_view),
    path('booking', bookingview.as_view()),
    path('menu', menuview.as_view()),
]
