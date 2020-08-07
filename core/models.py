from django.db import models

class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and `` modified`` fields.
    Default ordering is reverse-chronological 
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True
        ordering = ['-created', '-modified']
