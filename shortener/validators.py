from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
	url_validator = URLValidator()
	url1_invalid = False
	url2_invalid = False

	try:
		url_validator(value)
	except:
		url1_invalid = True

	if url1_invalid:
		value = "http://" + value

	try:
		url_validator(value)
	except:
		url2_invalid = True

	if url1_invalid and url2_invalid:
		raise ValidationError("Invalid URL")
	return value

def validate_dot_com(value):
	if not "com" in value:
			raise ValidationError("No com in the URL")
	return value
