from django.urls import path
from instamart.views import *

app_name='nothing'
urlpatterns=[
    path('icecream/',icecream,name='icecream'),
]