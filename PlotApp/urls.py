from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('listings/', listings, name='listings'),
    path('contact/', contact, name='contact'),
]