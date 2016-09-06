from django.db import models
from django.contrib.auth.models import User

# Create your models here.

LICENSES_COPYRIGHT = 'RIG'
LICENSES_COPYLEFT = 'LEF'
LICENSES_CC = 'CC'

LICENSES = (
    (LICENSES_COPYRIGHT, 'Copyright'),
    (LICENSES_COPYLEFT, 'Copyleft'),
    (LICENSES_CC, 'Creativecommons')
)

VISIBILITY_PUBLIC = 'PUB'
VISIBILITY_PRIVATE = 'PRI'

VISIBILITY = (
    (VISIBILITY_PUBLIC, 'Pública'),
    (VISIBILITY_PRIVATE, 'Privada')
)

class Photo (models.Model):


    owner = models.ForeignKey(User)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(null=True, blank=True)
    license = models.CharField(max_length=3, choices=LICENSES, default=LICENSES_CC)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=VISIBILITY_PUBLIC)

    def __str__(self):
        return self.name
