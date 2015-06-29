from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SenseisView.as_view(), name='home'),
    url(r'^(?P<slug>[\w-]+)/*$', views.SenseiView.as_view(), name='sensei'),
]