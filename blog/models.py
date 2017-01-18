from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title_text = models.CharField(max_length=200)
    body_text = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title_text

