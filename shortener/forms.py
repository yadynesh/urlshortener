from django import forms
from .validators import validate_url,validate_dot_com


class SubmitUrlForm(forms.Form):
	url = forms.CharField(label = "Submit URL", validators = [validate_url, validate_dot_com])

	#overriding the clean method. clean can be used to validate overall form
	# def clean(self):
	# 	cleaned_data = super(SubmitUrlForm, self).clean() 
	# 	url = cleaned_data.get('url')
	# 	url_validator = URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid url")
	# 	return url

	#clean_<nameOfField> is used to validate specific fields
	# def clean_url(self):

	# 	url = self.cleaned_data['url']
	# 	print(url)
	# 	if not "com" in url:
	# 		raise forms.ValidationError("No com in the url")
	# 	url_validator = URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid url")
	# 	return url