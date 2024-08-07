from django.contrib import admin
from django.urls import path, include
from Restaurant import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('admin/', admin.site.urls),
    path('api/',include('Restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),
]

