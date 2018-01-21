from django import forms

from .models import Series
from django.contrib.auth import get_user_model

User = get_user_model()

class SeriesModelForm(forms.ModelForm):
	class Meta:
		model = Series
		fields = ['owner',
			'title', 
			'creator',
			'productor',
			'rating'
		]

	def __init__(self, *args, **kwargs):
		super(SeriesModelForm, self).__init__(*args, **kwargs)
		superusers = User.objects.filter(is_superuser=True)
		self.fields["owner"].queryset = superusers

