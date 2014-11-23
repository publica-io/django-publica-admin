
try:
    from attrs.models import Attribute
except ImportError:
    pass
else:

    from django.contrib import admin
    from django.contrib.contenttypes import generic


    class AttrInline(generic.GenericTabularInline):
        '''Inline class for editing generic Attributes'''
        model = Attribute
        ct_field = 'content_type'
        ct_fk_field = 'object_id'
        extra = 0
