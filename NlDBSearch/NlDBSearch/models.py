from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    cat = models.TextField()
    act = models.TextField()
    utt = models.TextField()


    def __unicode__(self):
        return self.utt