from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProgramsView.as_view(), name='home'),
    url(r'^(?P<slug>[\w-]+)/*$', views.ProgramView.as_view(), name='program'),
]