# -*- coding: utf-8 -*-
"""Home views."""
from django.views import generic

from mentors.models import Mentor
from programs.models import Program
from senseis.models import Sensei

import random


class HomeView(generic.TemplateView):

    """Class-based view that handle the / URL."""

    template_name = 'home/home.html'

    def get_context_data(self):
        """Override get_context_data method from TemplateView to set
        all the new template variables.
        """
        context = super(HomeView, self).get_context_data()

        context['title'] = 'Dev.f'
        context['meta_description'] = 'Aprende a construir software en la ' +\
                                      'primera y más grande escuela de hackers ' +\
                                      'de México y LatAm'

        senseis_object_list = list(Sensei.objects.all())
        random.shuffle(senseis_object_list)
        context['senseis'] = senseis_object_list[:3]

        programs_object_list = list(Program.objects.all())
        random.shuffle(programs_object_list)
        context['programs'] = programs_object_list[:3]

        mentors_object_list = list(Mentor.objects.all())
        random.shuffle(mentors_object_list)
        context['mentors'] = mentors_object_list[:5]

        return context


class AboutView(generic.TemplateView):

    """Class-based view that handle the /about URL."""

    template_name = 'home/about.html'

    def get_context_data(self):
        """Override get_context_data method from TemplateView to set
        all the new template variables.
        """
        context = super(AboutView, self).get_context_data()

        context['title'] = 'Acerca de'
        context['meta_description'] = 'Conoce más sobre la escuela de hackers.'

        return context
