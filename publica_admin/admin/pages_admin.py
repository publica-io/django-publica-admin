
try:
    from django.contrib import admin
    from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

    from pages.models import *
except ImportError:
    pass
else:

    from django.contrib import admin
    from images_admin import ImageInline

    from ..mixins import *


    class PageAdmin(admin.ModelAdmin):
        
        inlines = [
            ImageInline,
        ]

        class Media:
            js = TinyMCETextMixin.Media.js


    admin.site.register(Page, PageAdmin)