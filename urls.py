from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
	url('^_ah/warmup/$', 'djangoappengine.views.warmup'),
	url('', include('blog.urls', namespace='blog')),
	# url(r'^account/', include('account.urls', namespace='account')),
	url('^account/', include('registration.backends.default.urls')),
	url('^account/', include('django.contrib.auth.urls')),
	url('', include('social_auth.urls')),
)

