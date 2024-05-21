from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'ship_sales_manage_sys/index.html')

def AI_view(request):
    return render(request, 'ship_sales_manage_sys/ai_view.html')
