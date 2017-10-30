from django.core.exceptions import ValidationError

CATEGORIES = ["Mexican","Asian","American"]

def validate_category(value):
	cat = value.capitalize()
	if not value in CATEGORIES and not cat in CATEGORIES:
		raise ValidationError("{value} not a valid category".format(value=value))