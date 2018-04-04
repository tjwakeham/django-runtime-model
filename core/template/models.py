from django.db import models as db


class Template(db.Model):
    """ Model class to save templates to the database """

    def __unicode__(self):
        return self.name

    id = db.CharField(max_length=255, primary_key=True)
    name = db.CharField(max_length=255)
    template = db.TextField(blank=True, null=True)






