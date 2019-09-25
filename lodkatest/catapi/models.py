from django.db import models

class Category(models.Model):

    name = models.CharField(
            max_length=255, blank=False, unique=True,
    )
    parent = models.ForeignKey(
            'self',
            related_name='children',
            blank=True,
            null=True,
            on_delete=models.CASCADE
    )

    def __str__(self):
        return f'name: {self.name} parent: {self.parent}'
