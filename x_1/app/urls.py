from django.urls import path
from app.views import MyView

urlpatterns = [
    path('get/', MyView.get),
    path('create_csv/', MyView.create_csv),
    path('gcalculate_csvet/', MyView.calculate_csv),
]