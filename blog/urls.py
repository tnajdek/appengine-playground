from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView
from models import Post
from forms import PostForm
from views import CreateView, UpdateView, DeleteView
from django.views.generic.simple import redirect_to

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
	url(r'^admin/$', redirect_to, {'url': '/admin/post/'}),
	url(r'^$', ListView.as_view(
		paginate_by=10,
		model=Post,
		template_name="blog/index.html"
		), name="index"
	),
	url(r'^(?P<slug>\w+)/$', DetailView.as_view(
		model=Post,
		slug_field='permalink',
		template_name="blog/post.html"
		), name="post"
	),
)
