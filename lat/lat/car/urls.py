from django.contrib.sitemaps.views import index
from django.urls import path, include

from lat.car.views import create_new, get_view, show_cars

urlpatterns = (
    # #/car/
    path('', index),
    #/car/ID/
    path('car/', get_view),
    #/car/int/ID/
    path('show/', show_cars),
    path('int/<car_id>/', show_cars),
)

# paths = (
#     '', '<car_id/', 'int/<int:car_id>/',
# )
#
# urlpatterns = [path(url, get_view) for url in paths]

# urlpatterns = ()
# urlpatterns += (path('', get_view),)
# urlpatterns += (path('<car_id>/', get_view),)
# urlpatterns += (path('int/<int:car_id', get_view),)
