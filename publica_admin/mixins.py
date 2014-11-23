from django.conf import settings


class TinyMCETextMixin(object):

	class Media:
	    js = [
	        '{}grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js'.format(settings.STATIC_URL),
	        '{}admin/tinymce/tinymce_setup.js'.format(settings.STATIC_URL),
	    ]