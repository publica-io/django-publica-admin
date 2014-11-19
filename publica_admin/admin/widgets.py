from django.contrib import admin

try:
	from widgets.models import *
except ImportError:
	pass
else:

	admin.register(Widget)