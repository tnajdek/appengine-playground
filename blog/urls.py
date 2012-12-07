from django.conf.urls.defaults import *
from django.views.generic import TemplateView, ListView
from models import Post
from forms import PostForm
from views import CreateView, UpdateView, DeleteView

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
	url(r'^$', TemplateView.as_view(template_name="home.html")),
)
