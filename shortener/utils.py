import random
import string

def code_generator(size = 6, chars = string.ascii_lowercase + string.digits):
	# _ is used when you dont want to use that variable
	return ''.join(random.choice(chars) for _ in range(size)) 


def generateShortcode(instance, size=6):

	new_code = code_generator(size = size)

	Klass = instance.__class__ 
	#we are doing this because models.py imports generateShortCode and thus we cannot import models.py

	if Klass.objects.filter(shortcode = new_code).exits() :
		generateShortcode(instance)
	else:
		return new_code
