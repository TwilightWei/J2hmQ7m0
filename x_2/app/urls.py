from django.urls import path
from app.views import MyView

urlpatterns = [
    path('get/', MyView.get),
]