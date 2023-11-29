from django.shortcuts import render
from django.http import JsonResponse
from .models import Resources

# Create your views here.

# def index(request):
#     resources = Resources.objects.all()
#     data = list(resources.values())
#     return JsonResponse(data, safe=False)
