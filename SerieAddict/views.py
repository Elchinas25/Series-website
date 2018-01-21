from django.views.generic import View

from django.shortcuts import render

from series.models import Series

class HomeView(View):
	def get(self, request):
		template_name = 'home.html'
		ordering = self.request.GET.get("ordering")
		if ordering == 'Newest':
			qs = Series.objects.order_by('-released')
		elif ordering == 'Oldest':
			qs = Series.objects.order_by('released')
		else:
			qs = Series.objects.order_by('-rating')
			ordering = 'Rating'
		print(ordering)
		context = {'qs': qs, 'ordering': ordering}
		return render(request, template_name, context)

