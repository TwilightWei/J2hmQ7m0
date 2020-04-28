from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from app.tasks import crawl

# Call carwl() when requested by GET
class MyView(View):
    def get(request):
        response = 'Finish crawling'
        crawl()
        return HttpResponse(response)