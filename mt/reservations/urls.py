from django.urls import path
from .views import create_reservation, reservation_detail, reservations_list

urlpatterns = [
    path('create/', create_reservation, name="create_reservation"),
    path('<int:id>/', reservation_detail, name="reservation_detail"),
    path('reservations/', reservations_list, name="reservations_list"),
]
