from django.shortcuts import render
from django.http import JsonResponse
from .models import Community

# Create your views here.
def index(request):
    community = Community.objects.all()
    data = list(community.values())
    return JsonResponse(data, safe=False)