from django import forms
from .models import RestaurantLocation
from .validators import validate_category

class RestaurantCreateForm(forms.Form):
	name = forms.CharField()
	location = forms.CharField(required=False)
	category = forms.CharField(required=False)

	# form validation
	def clean_name(self):
		name = self.cleaned_data.get("name")
		if not name:
			raise forms.ValidationError("Fill out name")
		return name
		
class RestaurantLocationCreateForm(forms.ModelForm):
	# category = forms.CharField(required=False, validators=[validate_category])
	class Meta:
		model = RestaurantLocation
		fields = [
			"name",
			"location",
			"category",
			"slug"
		]

	# form validation
	def clean_name(self):
		name = self.cleaned_data.get("name")
		if not name:
			raise forms.ValidationError("Fill out name")
		return name
