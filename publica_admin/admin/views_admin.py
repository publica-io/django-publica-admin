from django.contrib import admin

try:
    from views.models import *
except ImportError:
    pass
else:

    from images_admin import ImageInline

    from ..mixins import *


    class ViewLinkageInline(admin.StackedInline):
        fields = (
            'order',
            'content_type',
            'object_id',
            'enabled'
        )
        model = ViewLinkage
        extra = 0

        related_lookup_fields = {
            'generic': [['content_type', 'object_id'], ],
        }


    class ViewAdmin(TemplatesAdminMixin, PublicaModelAdminMixin, admin.ModelAdmin):
        exclude = (
            'preview_template',
        )
        fields = (
            'title',
            'slug',
            'short_title',
            'text',
            'template',
            'enabled'
        )
        inlines = [
            ViewLinkageInline,
            ImageInline,
        ]
        prepopulated_fields = {
            'slug': ('title', )
        }

        class Media:
            js = TinyMCETextMixin.Media.js


    admin.site.register(View, ViewAdmin)
