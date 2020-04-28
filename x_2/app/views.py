from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from app.tasks import crawl

# Call carwl() when requested by GET
class MyView(View):
    def get(request):
        response = 'Finish crawling'
        if request.method == 'GET':
            crawl()
        else:
            response = 'Request is not GET!'
        return HttpResponse(response)