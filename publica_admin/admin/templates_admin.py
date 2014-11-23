
try:
    from templates.models import *
except ImportError:
    pass
else:

    from django.contrib import admin

    admin.site.register(Template)
