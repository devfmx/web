"""Main URL's for the site."""

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

from home import views as home_views
from mentors import urls as mentors_urls
from programs import urls as programs_urls
from senseis import urls as senseis_urls

urlpatterns = [
    url(r'^$', home_views.HomeView.as_view(), name='home'),
    url(r'^about/$', home_views.AboutView.as_view(), name='about'),

    url(r'^aplica/$', RedirectView.as_view(url='https://devf.typeform.com/to/vGqumC'), name='apply'),

    url(r'^mentores/', include(mentors_urls, namespace='mentors')),
    url(r'^programas/', include(programs_urls, namespace='programs')),
    url(r'^senseis/', include(senseis_urls, namespace='senseis')),

    url(r'^admin/', include(admin.site.urls)),
    url('^markdown/', include('django_markdown.urls')),
]
