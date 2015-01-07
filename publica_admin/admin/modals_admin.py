
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
        extra = 0

        exclude = (
            'text',
            'short_title',
            'slug',
        )


    class ModalAdmin(PublicaModelAdminMixin, TemplatesAdminMixin, admin.ModelAdmin):
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
            AttrInline,
            ImageInline,
            ModalLinkAspectInline
        ]
        prepopulated_fields = {
            'slug': ('title', )
        }

        class Media:
            js = TinyMCETextMixin.Media.js


    admin.site.register(Modal, ModalAdmin)
