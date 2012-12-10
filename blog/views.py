from django.views.generic import *
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_auth import backends
# from django.db.models import Q


class FilteredListView(ListView):
	def get_queryset(self):
		if(self.request.user.is_authenticated()):
			# Sadly no support for OR filters in appengine :(
			# query = Q(visibility__in=[1, 2]) | Q(visibility=0, author=self.request.user)
			# nope
			# self.model.objects.all().exclude(~Q(author=self.request.user), visibility=0)
			return self.model.objects.filter(visibility__in=[1, 2])
		else:
			return self.model.objects.filter(visibility=2)


class FilteredDetailView(DetailView):
	def get_object(self):
		user = self.request.user
		object = super(FilteredDetailView, self).get_object()
		if(object.visibility == 2):
			return object
		if(user.is_authenticated and object.visibility == 1):
			return object
		if(user.is_authenticated and object.visibility == 0 and object.author == user):
			return object
		raise Http404(_(u"No %(verbose_name)s found matching the query")
			% {'verbose_name': queryset.model._meta.verbose_name})


class SuccessUrlMixin(object):
	def get_success_url(self):
		if('postaction' in self.request.POST and self.request.POST['postaction'] == "Save"):
			return reverse("%s:%s-editform" % ("blog", self.model.__name__.lower()), kwargs={"pk": self.object.id})
		else:
			return reverse("%s:%s-list" % ("blog", self.model.__name__.lower()))


class OwnershipMixin(object):
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user
		return super(OwnershipMixin, self).form_valid(form)


class CreateView(SuccessUrlMixin, OwnershipMixin, CreateView):
	pass


class UpdateView(SuccessUrlMixin, UpdateView):
	pass


class DeleteView(SuccessUrlMixin, DeleteView):
	pass


@login_required
def admin_home(request):
	potential_providers = backends.get_backends().keys()
	for social in request.user.social_auth.all():
		if social.provider in potential_providers:
			potential_providers = [x for x in potential_providers if x != social.provider]

	return render(request, 'admin_home.html', {
		'potential_providers': potential_providers
	})
