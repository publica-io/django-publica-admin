
try:
    from images.models import Image
except ImportError:
    pass
else:

    from django.contrib import admin
    from django.contrib.contenttypes import generic


    class ImageInline(generic.GenericStackedInline):
        '''Inline class for editing generic Attributes'''
        model = Image
        ct_field = 'content_type'
        ct_fk_field = 'object_id'
        extra = 0
