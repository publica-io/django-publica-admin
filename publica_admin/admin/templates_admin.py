
try:
    from django.contrib import admin

    from templates.models import *
except ImportError:
    pass
else:

    admin.site.register(Template)