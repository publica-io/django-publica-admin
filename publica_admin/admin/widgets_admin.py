
try:
    from widgets.models import *
except ImportError:
    pass
else:

    from django.contrib import admin
    from grappelli.forms import GrappelliSortableHiddenMixin
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

        exclude = (
            'preview_template',
            'template',
        )

        class Media:
            js = TinyMCETextMixin.Media.js

    class WidgetListItemInline(GrappelliSortableHiddenMixin, admin.StackedInline):

        model = WidgetListAspect
        extra = 0

        sortable_field_name = "order"


    class WidgetListAdmin(WidgetAdmin):

        exclude = (
            'featured',
            'preview_template',
            'template',
            'type',
        )
        inlines = [
            WidgetListItemInline,
        ]


    class WidgetMapPOIInlineAdmin(admin.StackedInline):

        exclude = (
            'preview_template',
        )

        model = WidgetMapPOI
        extra = 0


    class WidgetMapPOIAdmin(admin.ModelAdmin):

        inlines = [
            AttrInline,
            ImageInline,
        ]

    class WidgetMapAdmin(WidgetAdmin):

        exclude = (
            'preview_template',
            'template',
        )
        
        inlines = [
            AttrInline,
            ImageInline,
            WidgetLinkAspectInline
        ]


    admin.site.register(WidgetMap, WidgetMapAdmin)
    admin.site.register(WidgetMapPOI, WidgetMapPOIAdmin)
    admin.site.register(Widget, WidgetAdmin)
    admin.site.register(WidgetModal, WidgetModalAdmin)
    admin.site.register(WidgetList, WidgetListAdmin)
