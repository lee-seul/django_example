# from __future__ import unicode_literals # python2.X 지원용

from django.db import models
# from django.utils.encoding import python_2_unicode_compatible # python2.X 지원용

# @python2_unicode_compatible # python2.X 지원용
class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.title
