import os

from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

from app.config import MyViewConfig
from app.customer import Customer

# Create your views here.
class MyView(View):
    _config = None

    def get(request):
        response = "Folder existed"

        if request.method == 'GET':
            config = MyViewConfig()
            folder_dir = config.get_folder_dir()
            if not os.path.isdir(folder_dir):
                os.mkdir(folder_dir)
                response = "Folder created"
            return HttpResponse(response)
        
        else:
            response = "Request id not GET!"
            return HttpResponse(response)
    
    def create_csv(request):

        return HttpResponse('create_csv')
    
    def calculate_csv(request):

        return HttpResponse('calculate_csv')