# -*- coding: utf-8 -*-
from django.views import generic

from .models import Mentor

class MentorsView(generic.ListView):
	queryset = Mentor.objects.all()
	template_name = 'mentors/mentors.html'
	paginate_by = 20

	def get_context_data(self, **wkargs):
		context = super(MentorsView, self).get_context_data()
		context['title'] = 'Mentores'
		context['meta_description'] = 'Nuestra red de más de 50 mentores expertos en tecnología.'
		return context