from django.conf.urls import url
from . import views

urlpatterns = [
    url('api/v1/foods', views.foods),
    url('', views.index),
]
