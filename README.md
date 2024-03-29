What is it?
====================

Instant Potato Soup is a trivial, ultra-simple blogging software created for  research/learning purposes. It makes use of a non-rel version of Django and can be deployed to [app engine](https://appengine.google.com/) with 4 simple steps.

Functionality is very limited and as-is this application is probably useless for production. **Please note** that there is no concept of ACLs or permissions in this software i.e. every registered user can modify every post and registration is fully automated.

Features
========

* Create/Edit/Delete posts
* __All__ registered users have read/write access to all posts
* Support for markdown
* Support for social login
* Support for automatic registration with email-based activation

Instructions (Just add water!)
==============================

Instant Potato Soup can be deployed on Google app engine with the folowing steps:

1. Obtain source code & dependencies

    ```
    git clone https://github.com/tnajdek/appengine-playground.git
    git submodule init
    git submodule update
    ```

2. Edit app.yaml, put your application identifier and optionally version etc.
3. Create file sensitive_settings.py in root app folder with the following contents. SECRET_KEY can be anything but should be [unique and secret](https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY). Emails will be sent using app engine API hence DEFAULT_FROM_EMAIL needs [meet certain requirements](https://developers.google.com/appengine/docs/python/mail/sendingmail). Finally you will need to create apps with [Github](https://github.com/settings/applications/new), [Twitter](https://dev.twitter.com/apps/new) and [Facebook](https://developers.facebook.com/apps) and update values below:

    ```
    SECRET_KEY = '<give keyboard to your kid/cat/dog to get some random characters>'
    TWITTER_CONSUMER_KEY = ''
    TWITTER_CONSUMER_SECRET = ''
    FACEBOOK_APP_ID = ''
    FACEBOOK_API_SECRET = ''
    GITHUB_APP_ID = ''
    GITHUB_API_SECRET = ''

    DEFAULT_FROM_EMAIL = ''
    ```

4. Deploy to appengine:

    ```
    appcfg.py update .
    ```

That's it folks!

