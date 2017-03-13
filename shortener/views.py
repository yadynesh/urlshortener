from django.shortcuts import render,get_object_or_404
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
from .models import MagicUrl
from .forms import SubmitUrlForm
# Create your views here.

	
class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form  = SubmitUrlForm()
		context = {
			"title" : "MagicUrl.com",
			"form" : the_form
		}
		return render(request, 'shortener/home.html', context)

	def post(self, request, *args, **kwargs):
		print (request.POST)
		print (request.POST.get('url')) #url is the name of the input field in home.html
		template = "shortener/home.html"
		the_form  = SubmitUrlForm(request.POST)
		context = {
			"title" : "MagicUrl.com",
			"form" : the_form
		}
		
		if the_form.is_valid():
			new_url = the_form.cleaned_data.get("url")
			obj , created = MagicUrl.objects.get_or_create(url = new_url)
			if created:
				template = 'shortener/success.html'
				context = {
					'object' : obj
				}
				
			else:
				template = 'shortener/already-exists.html'
				
		return render(request, template, context)


class MagicCBView(View):

	def get(self, request,shortcode = None, *args , **kwargs):
		qs  = get_object_or_404(MagicUrl, shortcode=shortcode)
		return HttpResponseRedirect(qs.url)
		


# def magic_redirect_view(request,shortcode = None, *args , **kwargs):

# 	qs  = get_object_or_404(MagicUrl, shortcode=shortcode)
# 	return HttpResponseRedirect(qs.url)

# 		obj_url = None
# 	qs = MagicUrl.objects.filter(shortcode__iexact = shortcode.lower())
# 	if qs.exists() and qs.count() == 1:
# 		obj_url = qs.first().url
# 	try:
# 		qs = MagicUrl.objects.get(shortcode=shortcode)
# 	except:
# 		return HttpResponse("shortcode not found")