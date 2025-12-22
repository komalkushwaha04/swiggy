from django.urls import path
from food.views import *

app_name='willing'
urlpatterns=[
    path('birayani/',birayani,name='birayani'),
    path('aalu/',aalu,name='aalu'),
]