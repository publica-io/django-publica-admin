
try:
    from widgets.models import *
except ImportError:
    pass
else:

    from django.contrib import admin
    from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

    # Because Widgets depend on django-attrs & django-publica-images; we will assume these
    # imports will work; despite the defensive importing strategy found in those files.
    from attrs_admin import AttrInline
    from images_admin import ImageInline

    from ..mixins import *


    class WidgetAdmin(admin.ModelAdmin):

        inlines = [
            AttrInline,
            ImageInline,
        ]

        class Media:
            js = TinyMCETextMixin.Media.js


    class WidgetModalAdmin(WidgetAdmin):

        class Media:
            js = TinyMCETextMixin.Media.js


    class WidgetMapPOIInlineAdmin(admin.StackedInline):

        model = WidgetMapPOI
        extra = 0


    class WidgetMapAdmin(WidgetAdmin):

        inlines = [
            WidgetMapPOIInlineAdmin,
        ]


    admin.site.register(WidgetMap, WidgetMapAdmin)
    admin.site.register(WidgetMapPOI, WidgetAdmin)
    admin.site.register(Widget, WidgetAdmin)
    admin.site.register(WidgetModal, WidgetModalAdmin)
