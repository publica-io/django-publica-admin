
try:
    from django.contrib import admin
    from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

    from positions.models import *
except ImportError:
    pass
else:

    from django.contrib import admin

    from ..mixins import *


    class PositionAdmin(PublicaAdminMixin, admin.ModelAdmin):
        pass

    admin.site.register(Position, PositionAdmin)