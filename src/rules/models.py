from __future__ import unicode_literals

from django.db import models

from posts.models import Post
from comments.models import Comment

# Create your models here.
class Rule(models.Model):
    post = models.ForeignKey(Post)
    is_first = models.BooleanField(default=False)
    is_last = models.BooleanField(default=False)
    solution = models.ForeignKey(Comment,related_name='solution', default=False)
    response = models.ForeignKey(Comment,related_name='response', default=False)

    
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
