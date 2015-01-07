
try:
    from django.contrib import admin
    from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

    from positions.models import *
except ImportError:
    pass
else:

    from django.contrib import admin

    from ..mixins import *


    class PositionAdmin(PublicaModelAdminMixin, admin.ModelAdmin):
        fields = (
            'title',
            'slug',
            'short_title',
            'enabled'
        )
        prepopulated_fields = {
            'slug': ('title', )
        }

    admin.site.register(Position, PositionAdmin)
