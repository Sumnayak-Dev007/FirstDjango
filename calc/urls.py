from django.urls import path
from .views import (
    homie

)

urlpatterns = [
    path('',homie,name='home'),
]
