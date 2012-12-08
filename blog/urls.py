from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView, RedirectView
from models import Post
from forms import PostForm
from views import CreateView, UpdateView, DeleteView

# Django 1.3 doesn't get to be lazy!
try:
	from django.core.urlresolvers import reverse_lazy
except ImportError:
	from django.core.urlresolvers import reverse
	from django.utils.functional import lazy
	reverse_lazy = lambda x: lazy(reverse, str)(x)


urlpatterns = patterns('',
	# Somehow I don't like django contrib admin
	# Pluse it feels bit like cheating, so..
	url(r'^admin/post/$', ListView.as_view(
		paginate_by=10,
		model=Post
		), name="post-list"
	),
	url(r'^admin/post/createform/$', CreateView.as_view(
		model=Post,
		form_class=PostForm,
		), name="post-createform"
	),
	url(r'^admin/post/(?P<pk>\d+)/editform/$', UpdateView.as_view(
		model=Post,
		form_class=PostForm,
		), name="post-editform"
	),
	url(r'^admin/post/(?P<pk>\d+)/deleteform/$', DeleteView.as_view(
		model=Post
		), name="post-deleteform"
	),
	url(r'^admin/$', RedirectView.as_view(
		url=reverse_lazy('blog:post-list')
		), name="admin"
	),
	url(r'^$', ListView.as_view(
		paginate_by=5,
		model=Post,
		template_name="blog/index.html"
		), name="index"
	),
	url(r'^(?P<slug>[a-z0-9\-]+)/$', DetailView.as_view(
		model=Post,
		slug_field='permalink',
		template_name="blog/post.html"
		), name="post"
	),
)
