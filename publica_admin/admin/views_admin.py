from django.contrib import admin

try:
    from views.models import *
except ImportError:
    pass
else:

    from images_admin import ImageInline


    class ViewLinkageInline(admin.StackedInline):

        model = ViewLinkage
        extra = 0

        autocomplete_lookup_fields = {
            'generic': [['content_type', 'object_id'], ],
        }

    class ViewAdmin(admin.ModelAdmin):

        inlines = [
            ViewLinkageInline,
            ImageInline,
        ]

    admin.site.register(View, ViewAdmin)