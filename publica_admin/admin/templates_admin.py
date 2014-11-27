
try:
    from templates.models import *
except ImportError:
    pass
else:

    from django.contrib import admin

    from ..mixins import *

    
    class TemplateAdmin(PublicaAdminMixin, admin.ModelAdmin):
    	pass


    admin.site.register(Template, TemplateAdmin)
