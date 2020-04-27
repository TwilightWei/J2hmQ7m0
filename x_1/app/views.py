import os
import csv

from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

from app.config import MyViewConfig
from app.customer import Customer

# Create your views here.
class MyView(View):
    def get(request):
        response = 'Folder existed'
        if request.method == 'GET':
            config = MyViewConfig()
            folder_dir = config.get_folder_dir()
            if not os.path.isdir(folder_dir):
                os.mkdir(folder_dir)
                response = 'Folder created'
        else:
            response = 'Request id not GET!'
        return HttpResponse(response)
    
    def create_csv(request):
        response = 'CSV created'
        if request.method == 'GET':
            config = MyViewConfig()
            customer = Customer()
            folder_dir = config.get_folder_dir()
            csv_name = config.get_csv_name()
            customers = customer.generate_customer()
            with open(folder_dir+'/'+csv_name, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(['customer_id', 'customer_name', 'customer_mobile', 'frequency'])
                for key in customers:
                    response = key
                    writer.writerow([customers[key]['customer_id'], customers[key]['customer_name'], key, customers[key]['frequency']])
        else:
            response = 'Request id not GET!'
        return HttpResponse(response)
    
    def calculate_csv(request):
        response = ''
        
        return HttpResponse('calculate_csv')