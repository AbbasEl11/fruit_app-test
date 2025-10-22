from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
# Create your views here.


def send_fruits(request):
    fruits = [{"name": "Apfel", "color": "Rot", "weight": "150g", "ordered": False},
              {"name": "Banane", "color": "Gelb",
                  "weight": "120g", "ordered": True},
              {"name": "Kirsche", "color": "Rot",
                  "weight": "1.5kg", "ordered": True},
              {"name": "Birne", "color": "Grün",
                  "weight": "5kg", "ordered": False},
              ]
    if request.method == "GET":
        return render(request, "fruit_app/fruitlist.html", {"fruits": fruits})
        return JsonResponse(fruits, safe=False)
    raise Http404("fruit not found")


def info_fruits(request):
    return render(request, "fruit_app/info.html")
