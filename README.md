What is it?
====================

Instant Potato Soup is a trivial, ultra-simple blogging software created for  research/learning purposes. It makes use of a non-rel version of Django and can be deployed to [https://appengine.google.com/](app engine) with 4 simple steps. 

Functionality is very limited and as-is this application is probably useless for production.

Features
========

* Create/Edit/Delete posts
* Support for markdown
* Support for social login

Instructions (Just add water!)
===============

Instant Potato Soup can be deployed on Google app engine with the folowing steps

# Obtain source code & dependencies 
	git clone https://github.com/tnajdek/appengine-playground.git
	git submodule init
	git submodule update

# Edit app.yaml, put your application identifier and optionally version etc.
# Create file sensitive_settings.py in root app folder with the following contents. SECRET_KEY can be anything but should be [https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY](unique and secret). You will need to create apps with [https://dev.twitter.com/apps/new](Twitter) and [https://developers.facebook.com/apps](Facebook) and update values below:

	SECRET_KEY = '<give keyboard to your kid/cat/dog to get some random characters>'

	TWITTER_CONSUMER_KEY = ''
	TWITTER_CONSUMER_SECRET = ''
	FACEBOOK_APP_ID = ''
	FACEBOOK_API_SECRET = ''


# Deploy to appengine:
	appcfg.py update .

That's it folks!

