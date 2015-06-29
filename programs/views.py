# -*- coding: utf-8 -*-
from django.views import generic

from .models import Program

class ProgramsView(generic.ListView):
	queryset = Program.objects.published()
	template_name = 'programs/programs.html'
	paginate_by = 15

	def get_context_data(self, **wkargs):
		context = super(ProgramsView, self).get_context_data()
		context['title'] = 'Programas'
		context['meta_description'] = 'Programas de Devf'
		return context

class ProgramView(generic.DetailView):
	model = Program
	template_name = 'programs/program.html'

	def get_context_data(self, **wkargs):
		context = super(ProgramView, self).get_context_data()
		context['title'] = context['program'].name
		context['meta_description'] = context['program'].short_description[:156] + '...'
		return context