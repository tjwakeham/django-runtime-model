## Runtime Django models

This Django application allows the runtime creation of database tables, admin templates and forms for the manipulation
of databases through the Django Admin interface.

It's intended use was for creation of forms that allowed full logging and reporting of data entered.  As it generates
Django models and caches them, there is limited performance impact.

While it is entirely possible to have a foreign key to a non dynamic model, the reverse should not be done as the 
runtime model may not be available at the time Django links models.

Requires - `grapelli` and `grapelli_nested` for the admin interface.

There are a couple of apps included which demonstrate adding new field types. 
