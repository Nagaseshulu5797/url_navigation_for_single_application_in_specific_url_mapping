from django.urls import path

from app.views import *

app_name='seshulu'

urlpatterns=[
    path('hai/',hai,name='hai'),
    path('hello/',hello,name='hello'),
]