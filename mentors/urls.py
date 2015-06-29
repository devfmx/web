from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.MentorsView.as_view(), name='home'),
]