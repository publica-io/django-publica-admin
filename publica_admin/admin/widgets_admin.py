
try:
    from widgets.models import *
except ImportError:
    pass
else:

    from django.contrib import admin
    from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

    from attrs_admin import AttrInline
    from images_admin import ImageInline

    from ..mixins import *


    class WidgetLinkAspectInline(admin.StackedInline):

        model = WidgetLinkAspect
        extra = 0

        exclude = (
            'text',
            'short_title',
            'slug',
        )


    class WidgetAdmin(TemplatesAdminMixin, admin.ModelAdmin):

        inlines = [
            AttrInline,
            ImageInline,
            WidgetLinkAspectInline
        ]

        exclude = (
            'preview_template',
        )

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
            AttrInline,
            ImageInline,
            WidgetLinkAspectInline
        ]


    admin.site.register(WidgetMap, WidgetMapAdmin)
    admin.site.register(WidgetMapPOI, WidgetAdmin)
    admin.site.register(Widget, WidgetAdmin)
    admin.site.register(WidgetModal, WidgetModalAdmin)
