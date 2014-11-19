from django.contrib import admin

try:
    from menus.models import *
except ImportError:
    pass
else:

    class MenuItemInline(admin.StackedInline):

        model = MenuItem

        def formfield_for_foreignkey(self, db_field, request, **kwargs):

            field = super(MenuItemInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

            if db_field.name == "parent":
                if request._obj_ is not None:
                    field.queryset = field.queryset.filter(menu = request._obj_)  
                else:
                    field.queryset = field.queryset.none()

            return field


    class MenuAdmin(admin.ModelAdmin):

        inlines = [
            MenuItemInline
        ]

        def get_form(self, request, obj=None, **kwargs):
            # just save obj reference for future processing in Inline
            request._obj_ = obj
            return super(MenuAdmin, self).get_form(request, obj, **kwargs)


    admin.site.register(Menu, MenuAdmin)