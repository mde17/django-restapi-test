from __future__ import unicode_literals

from django.db import models

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Movie(models.Model):
    EXPIRED = 0
    NOW_SHOWING = 1
    COMING_SOON = 1
    
    STATUS = (
        (EXPIRED, _('Expired')),
        (NOW_SHOWING, _('Now Showing')),
        (COMING_SOON, _('Coming Soon'))
    )
    
    title = models.CharField(max_length=100, blank=False)
    status = models.SmallIntegerField(choices=STATUS,
                                      default=EXPIRED)
    synopsis = models.TextField(max_length=1000, blank=True)
    
    
#    def save(self, *args, **kwargs):
##        print 'saving...'
##        print args
##        self.title = 'test3'
#        super(Movie, self).save(*args, **kwargs)