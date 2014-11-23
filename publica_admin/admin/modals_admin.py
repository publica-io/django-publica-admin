
try:
    from modals.models import *
except ImportError:
    pass
else:

    from django.contrib import admin
    from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

    # Because Modals depend on django-attrs & django-publica-images; we will assume these
    # imports will work; despite the defensive importing strategy found in those files.
    from attrs_admin import AttrInline
    from images_admin import ImageInline

    from ..mixins import *


    class ModalAdmin(admin.ModelAdmin):
        
        inlines = [
            AttrInline,
            ImageInline,
        ]

        class Media:
            js = TinyMCETextMixin.Media.js


    admin.site.register(Modal, ModalAdmin)