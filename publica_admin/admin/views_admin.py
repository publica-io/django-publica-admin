from django.contrib import admin

try:
    from views.models import *
except ImportError:
    pass
else:

    class ViewLinkageInline(admin.StackedInline):

        model = ViewLinkage
        extra = 0

    class ViewAdmin(admin.ModelAdmin):

        inlines = [
            ViewLinkageInline,
        ]

    admin.site.register(View, ViewAdmin)