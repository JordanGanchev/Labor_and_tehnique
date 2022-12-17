from django.contrib.sitemaps.views import index
from django.urls import path, include

from lat.car.views import car_now, create_new, get_value

urlpatterns = (
    path('', car_now),
    path('new/', create_new),
    path('value/', get_value),
)