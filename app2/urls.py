from app2.views import*
from django.urls import path
app2_name='anything'
urlpatterns=[
    path('app2_first/', app2_first,name='app2_first'),
    path('app2_second/',app2_second,name='app2_second'),
]