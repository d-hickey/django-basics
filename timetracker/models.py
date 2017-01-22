from __future__ import unicode_literals

from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class TimeEntry(models.Model):
    user = models.ForeignKey(User)
    rec_time = models.TimeField('Time spent on this project')
    rec_date = models.DateField('Date this project was worked on')
    choices = (('YT','Watching Youtube'),('FB', 'Checking Facebook'), ('PR', 'Pretending to work'), ('SM', 'Smoke break'))
    project = models.CharField(choices=choices, max_length=4, default='PR')

    def __str__(self):
        return self.project
