from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/foods/(?P<pk>[0-9]+)$', views.get_delete_update_food, name='get_delete_update_food'),
    url(r'^api/v1/foods/$', views.get_post_foods, name='get_post_foods'),
    url('api/v1/foods', views.foods),
    # url('', views.index),
]
