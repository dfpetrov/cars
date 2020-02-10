from django.urls import path
from django.conf.urls import url
from django.urls import reverse_lazy

from . import views

app_name = 'appmain'

urlpatterns = [
    url(r'^$', views.CarList.as_view(), name='index'),
]