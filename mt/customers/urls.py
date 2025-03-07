from django.urls import path
from .views import customer_list, create_customer, customer_detail

urlpatterns = [
    
    path('create/', create_customer, name="create-customer"),
    path('<int:id>/', customer_detail, name="customer-detail"),
    path('', customer_list, name='customers_list'),
    
]
