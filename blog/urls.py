from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView, TemplateView
from models import Post
from forms import PostForm
from views import CreateView, UpdateView, DeleteView, FilteredListView, FilteredDetailView, admin_home
from django.contrib.auth.decorators import login_required

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
	url(r'^admin/post/$', login_required(ListView.as_view(
		paginate_by=10,
		model=Post
		)), name="post-list"
	),
	url(r'^admin/post/createform/$', login_required(CreateView.as_view(
		model=Post,
		form_class=PostForm,
		)), name="post-createform"
	),
	url(r'^admin/post/(?P<pk>\d+)/editform/$', login_required(UpdateView.as_view(
		model=Post,
		form_class=PostForm,
		)), name="post-editform"
	),
	url(r'^admin/post/(?P<pk>\d+)/deleteform/$', login_required(DeleteView.as_view(
		model=Post
		)), name="post-deleteform"
	),
	url(r'^admin/$', admin_home, name="admin"),
	url(r'^$', FilteredListView.as_view(
		paginate_by=5,
		model=Post,
		template_name="blog/index.html"
		), name="index"
	),
	url(r'^(?P<slug>[a-z0-9\-]+)/$', FilteredDetailView.as_view(
		model=Post,
		slug_field='permalink',
		template_name="blog/post.html"
		), name="post"
	),
	url('^login/error/$', TemplateView.as_view(
		template_name="login-error.html"
	)),
)
