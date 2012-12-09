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
# To enable social login, create file sensitive_settings.py in root app folder with the following contents. You will need to create apps with [https://dev.twitter.com/apps/new](Twitter) and [https://developers.facebook.com/apps](Facebook) and update values below:

	TWITTER_CONSUMER_KEY = ''
	TWITTER_CONSUMER_SECRET = ''
	FACEBOOK_APP_ID = ''
	FACEBOOK_API_SECRET = ''


# Deploy to appengine:
	appcfg.py update .

That's it folks!

