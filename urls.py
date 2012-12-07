from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
	url('^_ah/warmup$', 'djangoappengine.views.warmup'),
	url(r'', include('blog.urls', namespace='blog')),
	url(r'', include('social_auth.urls')),
)
