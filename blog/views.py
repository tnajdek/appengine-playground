from django.views.generic import *
from django.core.urlresolvers import reverse
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_auth import backends


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
