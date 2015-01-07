
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
        fields = (
            'title',
            'slug',
            'short_title',
            'text',
            'template',
            'featured',
            'enabled'
        )
        inlines = [
            AttrInline,
            ImageInline,
            WidgetLinkAspectInline
        ]
        prepopulated_fields = {
            'slug': ('title', )
        }

        class Media:
            js = TinyMCETextMixin.Media.js


    class WidgetModalAdmin(WidgetAdmin):
        fields = (
            'title',
            'slug',
            'short_title',
            'text',
            'content_type',
            'object_id',
            'featured',
            'enabled'
        )

        class Media:
            js = TinyMCETextMixin.Media.js

    class WidgetListItemInline(GrappelliSortableHiddenMixin, admin.StackedInline):

        model = WidgetListAspect
        extra = 0

        sortable_field_name = "order"


    class WidgetListAdmin(WidgetAdmin):
        fields = (
            'title',
            'slug',
            'short_title',
            'text',
            'enabled'
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
        fieldsets = (
            (None, {
                'fields': ('title', 'slug', 'short_title', 'text', 'widget')
            }),
            ('Location', {
                'fields': ('activity', 'venue', 'x', 'y')
            }),
        )
        inlines = [
            AttrInline,
            ImageInline,
        ]

    class WidgetMapAdmin(WidgetAdmin):
        fields = (
            'title',
            'slug',
            'short_title',
            'text',
            'enabled'
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
