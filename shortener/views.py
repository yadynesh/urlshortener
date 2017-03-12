from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
def magic_redirect_view(request, *args , **kwargs):
	return HttpResponse("Yo this is MagicUrl")

class MagicCBView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse("Yo this is MagicCBView")

