from django.shortcuts import render
from django.http import JsonResponse
from .models import Table
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_table(request):
    if request.method == "POST":
        data = json.loads(request.body)
        table = Table.objects.create(number=data["number"], seats=data["seats"])
        return JsonResponse({"id": table.id, "number": table.number, "seats": table.seats})

def tables_list(request):
    return render(request, 'tables_list.html')