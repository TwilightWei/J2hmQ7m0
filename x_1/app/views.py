import os
import csv
import statistics

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View

from app.config import MyViewConfig
from app.customer import Customer

class MyView(View):
    # Create a folder in specific dir
    def get(request):
        response = 'Folder existed'
        if request.method == 'GET':
            config = MyViewConfig()
            folder_dir = config.get_folder_dir()
            if not os.path.isdir(folder_dir):
                os.mkdir(folder_dir)
                response = 'Folder created'
        else:
            response = 'Request is not GET!'
        return HttpResponse(response)
    
    # Create a csv in the folder and store customer data in it
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
                    writer.writerow([customers[key]['customer_id'], customers[key]['customer_name'], key, customers[key]['frequency']])
        else:
            response = 'Request is not GET!'
        return HttpResponse(response)
    
    # Calculate the median, mode and mean of frequency from the csv file
    def calculate_csv(request):
        response = {}
        if request.method == 'GET':
            config = MyViewConfig()
            folder_dir = config.get_folder_dir()
            csv_name = config.get_csv_name()
            frequency_list = []
            median = None
            mode = None
            mean = None
            with open(folder_dir+'/'+csv_name, 'r', newline='') as csv_file:
                rows = csv.DictReader(csv_file)
                for row in rows:
                    frequency_list.append((int(row['frequency'])))
            frequency_list.sort()
            median = statistics.median(frequency_list)
            try:
                mode = statistics.mode(frequency_list)
            except:
                print('No mode exists.')
            mean = round(statistics.mean(frequency_list), 5)
            response['median'] = median
            response['mode'] = mode
            response['mean'] = mean
        else:
            response['error'] = 'Request is not GET!'
        return JsonResponse(response)