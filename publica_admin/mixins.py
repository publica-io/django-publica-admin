from django.conf import settings
from django.core.urlresolvers import reverse 
from django.contrib.contenttypes.models import ContentType

try:
    from polymorphic import PolymorphicModel
except ImportError:
    PolymorphicModel = None

from entropy.mixins import *



# Model Mixins


class PublicaAdminMixin(models.Model):
    '''
    A class with common Admin URLs and functions
    '''

    class Meta:
        abstract = True

    def get_add_url(self):
        return reverse(
            'admin:{}_{}_add'.format(self._meta.app_label, self._meta.model_name),
        )

    def get_change_url(self):
        return reverse(
            'admin:{}_{}_change'.format(self._meta.app_label, self._meta.model_name),
            args=(self.id, )
        )

    def get_change_list_url(self):
        return reverse(
            'admin:{}_{}_changelist'.format(self._meta.app_label, self._meta.model_name)
        )

    def get_history_url(self):
        return reverse(
            'admin:{}_{}_history'.format(self._meta.app_label, self._meta.model_name),
            args=(self.id, )
        )


# Model Admin Mixins


list_display_order = [
    TitleMixin,
    NameMixin,
    SlugMixin,
    LinkURLMixin,
    EnabledMixin,
]

field_display_order = [
    EnabledMixin,
    TitleMixin,
    NameMixin,
    SlugMixin
]

class PublicaModelAdminMixin(object):
    '''
    The PublicaModelAdminMixin quite magically assembles ModelAdmin arguments
    depending on the existence of Entropy mixins.

    The goal is to produce a very consistent and magical admin based on
    predetermined entropy mixins.
    '''

    def get_list_display(self, request):
        '''
        Assemble a list_display based on the existence
        of Entropy mixins.
        '''
        for mixin in list_display_order:

            # non-poly
            if mixin in self.model.__bases__:
                for field in mixin._meta.fields:
                    if field.name not in self.list_display:
                        self.list_display += (field.name, )

            if PolymorphicModel is not None:
                # If we have polymorphic models; recurse and try 
                # to discover the base class.
                bases = [b for b in self.model.__bases__
                    if issubclass(b, PolymorphicModel)
                    and not b._meta.abstract and not b._meta.proxy]
                for base in bases:
                    for mixin_base in base.__bases__:
                        if mixin == mixin_base:
                            for field in mixin._meta.fields:
                                if field.name not in self.list_display:
                                    self.list_display += (field.name, )


        return super(PublicaModelAdminMixin, self).get_list_display(request)


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
            field.queryset = field.queryset.filter(_name__istartswith = self.model._meta.app_label)

        return field
