# -*- coding: utf-8 -*-
from django.views import generic

from .models import Sensei

class SenseisView(generic.ListView):
	queryset = Sensei.objects.all()
	template_name = 'senseis/senseis.html'
	paginate_by = 15

	def get_context_data(self, **wkargs):
		context = super(SenseisView, self).get_context_data()
		context['title'] = 'Senseis'
		context['meta_description'] = 'Conoce al equipo de instructores de Dev.F.'
		return context

class SenseiView(generic.DetailView):
	model = Sensei
	template_name = 'senseis/sensei.html'

	def get_context_data(self, **wkargs):
		context = super(SenseiView, self).get_context_data()
		context['title'] = context['sensei'].first_name
		context['meta_description'] = context['sensei'].short_description[:156] + '...'
		return context