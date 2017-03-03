from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contact, name='posts_list')
]