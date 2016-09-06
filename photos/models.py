from django.db import models

# Create your models here.

class Photo (models.Model):

    LICENSES = (
        ('RIG', 'Copyright'),
        ('LEF', 'Copyleft'),
        ('CC', 'Creativecommons')
    )

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField()
    license = models.CharField(max_length=3, choices=LICENSES)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)