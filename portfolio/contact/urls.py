from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.contact, name='contact'),
    url(r'^show/', views.messages_list, name='messages_list')
]