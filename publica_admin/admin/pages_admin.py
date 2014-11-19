
try:
    from django.contrib import admin
    from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

    from pages.models import *
except ImportError:
    pass
else:

    admin.site.register(Page)