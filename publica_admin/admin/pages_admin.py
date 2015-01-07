
try:
    from pages.models import *
except ImportError:
    pass
else:

    from django.contrib import admin
    from grappelli.forms import GrappelliSortableHiddenMixin

    from images_admin import ImageInline
    from views.models import PageView

    from ..mixins import *


    class PageViewAdminInline(GrappelliSortableHiddenMixin, admin.StackedInline):

        model = PageView
        extra = 0

        sortable_field_name = "order"


    class PageAdmin(PublicaModelAdminMixin, TemplatesAdminMixin, admin.ModelAdmin):
        exclude = (
            'template',
            'preview_template',
        )
        fields = (
            'title',
            'slug',
            'short_title',
            'text',
            'enabled'
        )
        inlines = [
            PageViewAdminInline,
            ImageInline,
        ]
        prepopulated_fields = {
            'slug': ('title', )
        }

        class Media:
            js = TinyMCETextMixin.Media.js


    admin.site.register(Page, PageAdmin)
