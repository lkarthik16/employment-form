from django.urls import path
from .views import home, employment_form, success

urlpatterns = [
    path('', home, name='home'),  # Homepage
    path('employment_form/', employment_form, name='employment_form'),
    path('success/', success, name='success'),
]