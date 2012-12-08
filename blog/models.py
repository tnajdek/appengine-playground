from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=50)


class Post(models.Model):
	VISIBILITY_OPTIONS = (
		(0, 'Private'),
		(1, 'Visible to registered users'),
		(2, 'Public')
	)
	title = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
	visibility = models.PositiveSmallIntegerField(choices=VISIBILITY_OPTIONS, default=0)
	text = models.TextField()
	author = models.ForeignKey(User)
	permalink = models.CharField(max_length=200, unique=True)
	class Meta:
		ordering = ['-date_created']


class Tag(models.Model):
	article = models.ForeignKey(Post)
	title = models.CharField(max_length=200)
