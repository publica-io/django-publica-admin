
try:
    from django.contrib import admin
    from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

    from widgets.models import *
except ImportError:
    pass
else:

    class WidgetMapPOIInlineAdmin(admin.StackedInline):

        model = WidgetMapPOI
        extra = 0

    class WidgetMapAdmin(admin.ModelAdmin):

        inlines = [
            WidgetMapPOIInlineAdmin,
        ]

    admin.site.register(WidgetMap, WidgetMapAdmin)
    admin.site.register(Widget)