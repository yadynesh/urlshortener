from django.shortcuts import render,get_object_or_404
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect
from .models import MagicUrl
# Create your views here.

	
class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'shortener/home.html', {})


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