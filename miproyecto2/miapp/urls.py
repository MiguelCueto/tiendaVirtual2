from django.conf.urls import url
from miapp import views

urlpatterns = [
   url(r'^$', views.indice, name='indice'),
]
