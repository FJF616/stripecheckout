Stripe checkout implemented with Django.  The backend handles the transaction and uses templates.  NOTE: The version of Django used in this repo is deprecated and will cause some breaking changes if upgraded to current version.  this project is taken directly from this easy to follow tutorial: https://testdriven.io/django-stripe-tutorial  

you will need your stripe api test keys for the check out method. some extra dependencies were also added that were not in the article.
whitnoise module is also added in but not used, I needed it for something else but if you don't then just remove it out of the requirements.txt

UPDATE: this has been updated to Django 2.1.1