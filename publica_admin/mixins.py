from django.conf import settings


class TinyMCETextMixin(object):

    class Media:
        js = [
            '{}grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'.format(settings.STATIC_URL),
            '{}admin/tinymce/tinymce_setup.js'.format(settings.STATIC_URL),
        ]


class TemplatesAdminMixin(object):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        field = super(TemplatesAdminMixin, self).formfield_for_foreignkey(db_field, request, **kwargs)

        if db_field.name in ('template', 'preview_template',):
            field.queryset = field.queryset.filter(name__istartswith = self.model._meta.app_label)

        return field
