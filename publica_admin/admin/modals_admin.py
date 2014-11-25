
try:
    from modals.models import *
except ImportError:
    pass
else:

    from django.contrib import admin
    from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

    from attrs_admin import AttrInline
    from images_admin import ImageInline

    from ..mixins import *


    class ModalLinkAspectInline(admin.StackedInline):

        model = ModalLinkAspect


    class ModalAdmin(TemplatesAdminMixin, admin.ModelAdmin):
        
        inlines = [
            AttrInline,
            ImageInline,
            ModalLinkAspectInline
        ]

        class Media:
            js = TinyMCETextMixin.Media.js


    admin.site.register(Modal, ModalAdmin)
