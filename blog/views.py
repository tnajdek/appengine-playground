from django.views.generic import *
from django.core.urlresolvers import reverse


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
