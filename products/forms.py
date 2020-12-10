from django import forms
from . import models

class CreateArticle(forms.ModelForm):
	class Meta:
		model = models.Product
		fields = ['title','body','url','image','icon']
