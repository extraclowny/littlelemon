from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'), namespace = 'rest_framework'),
    path('comments', views.form_view),
    # path('booking', bookingview.as_view()),
    # path('menu', menuview.as_view()),
    path('menuview', views.MenuItemView.as_view()),
    path('menuview/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('bookingview', views.BookingView.as_view()),
    # path('bookingview/<int:pk>', views.SingleBookingView.as_view()),
]
