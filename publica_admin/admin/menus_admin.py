
try:
    from menus.models import *
except ImportError:
    pass
else:
    from django.contrib import admin
    from grappelli.forms import GrappelliSortableHiddenMixin

    from images_admin import ImageInline

    from ..mixins import PublicaModelAdminMixin
    

    class MenuItemInline(GrappelliSortableHiddenMixin, admin.StackedInline):

        exclude = (
            'is_featured',
        )
        extra = 0
        model = MenuItem

        sortable_field_name = "order"

        def formfield_for_foreignkey(self, db_field, request, **kwargs):

            field = super(MenuItemInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

            if db_field.name == "parent":
                if request._obj_ is not None:
                    field.queryset = field.queryset.filter(menu = request._obj_)  
                else:
                    field.queryset = field.queryset.none()

            return field


    class MenuAdmin(PublicaModelAdminMixin, admin.ModelAdmin):

        inlines = [
            MenuItemInline
        ]

        def get_form(self, request, obj=None, **kwargs):
            # just save obj reference for future processing in Inline
            request._obj_ = obj
            return super(MenuAdmin, self).get_form(request, obj, **kwargs)


    class LinkAdmin(PublicaModelAdminMixin, admin.ModelAdmin):

        related_lookup_fields = {
            'generic': [['content_type', 'object_id'], ],
        }

        inlines = [
            ImageInline,
        ]


    admin.site.register(Menu, MenuAdmin)
    admin.site.register(Link, LinkAdmin)