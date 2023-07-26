from app1.views import *
from django.urls import path
app1_name='something'
urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]