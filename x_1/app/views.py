from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

# Create your views here.
class MyView(View):
    - _config = None

    def get(request):

        return HttpResponse('get')
    
    def create_csv(request):

        return HttpResponse('create_csv')
    
    def calculate_csv(request):

        return HttpResponse('calculate_csv')