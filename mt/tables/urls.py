from django.urls import path
from .views import create_table, tables_list

urlpatterns = [
    path('tables/', tables_list, name="tables_list"),
    path('create/', create_table, name="create_table"),
]
