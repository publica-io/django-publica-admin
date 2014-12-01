# -*- coding: utf-8 -*-

try:
    from meta.models import MetatagModelInstance, MetatagPath
except ImportError:
    pass
else:
    from django.contrib import admin

    META_FIELDSETS = (
        ('Metatags', {
            'fields': ('author', 'description', 'keywords')
        }),
        ('Open Graph Metadata', {
            'fields': ('url', 'title', 'image', 'type', 'site_name')
        })
    )

    class MetatagModelInstanceAdmin(admin.ModelAdmin):
        fieldsets = (
            (None, {
                'fields': ('content_type', 'object_id')
            }),
        ) + META_FIELDSETS
        related_lookup_fields = {
            'generic': (['content_type', 'object_id'], )
        }

    class MetatagModelPathAdmin(admin.ModelAdmin):
        fieldsets = (
            (None, {
                'fields': ('path', )
            }),
        ) + META_FIELDSETS

    admin.site.register(MetatagModelInstance, MetatagModelInstanceAdmin)
    admin.site.register(MetatagPath, MetatagModelPathAdmin)
