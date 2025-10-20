from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
# Create your views here.


def send_fruits(request):
    fruits = [{"name": "Apple", "color": "Green", "weight": "150g"},
              {"name": "Banana", "color": "Yellow", "weight": "120g"},
              {"name": "Ananas", "color": "Brown", "weight": "1.5kg"},
              {"name": "Watermelon", "color": "Green/Red", "weight": "5kg"},
              ]
    if request.method == "GET":
        return JsonResponse(fruits, safe=False)
    raise Http404("fruit not found")
