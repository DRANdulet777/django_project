from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Reservation
from customers.models import Customer
from tables.models import Table

@csrf_exempt
def create_reservation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        customer = Customer.objects.get(id=data["customer_id"])
        table = Table.objects.get(id=data["table_id"])
        
        # Проверка на существующую бронь
        if Reservation.objects.filter(table=table, date=data["date"]).exists():
            return JsonResponse({"error": "Table is already reserved on this date"}, status=400)

        reservation = Reservation.objects.create(
            customer=customer, table=table, date=data["date"], status="pending"
        )
        return JsonResponse({"id": reservation.id, "status": reservation.status})

def reservation_detail(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    return JsonResponse({
        "id": reservation.id,
        "customer": reservation.customer.name,
        "table": reservation.table.number,
        "date": reservation.date,
        "status": reservation.status
    })
