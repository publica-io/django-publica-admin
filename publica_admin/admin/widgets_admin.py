
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


    class WidgetAdmin(PublicaAdminMixin, TemplatesAdminMixin, admin.ModelAdmin):

        exclude = (
            'preview_template',
        )

        inlines = [
            AttrInline,
            ImageInline,
        ]

        class Media:
            js = TinyMCETextMixin.Media.js


    class WidgetModalAdmin(WidgetAdmin):

        exclude = (
            'preview_template',
        )

        class Media:
            js = TinyMCETextMixin.Media.js


    class WidgetMapPOIInlineAdmin(admin.StackedInline):

        exclude = (
            'preview_template',
        )

        model = WidgetMapPOI
        extra = 0


    class WidgetMapAdmin(WidgetAdmin):

        exclude = (
            'preview_template',
        )
        
        inlines = [
            WidgetMapPOIInlineAdmin,
        ]


    admin.site.register(WidgetMap, WidgetMapAdmin)
    admin.site.register(WidgetMapPOI, WidgetAdmin)
    admin.site.register(Widget, WidgetAdmin)
    admin.site.register(WidgetModal, WidgetModalAdmin)
