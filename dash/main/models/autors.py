
from django.db import models


class Autors(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, unique=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=False, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        name = self.name
        return '{}'.format(name)

    class Meta:
        db_table = 'autors'
        verbose_name_plural = 'Autors'
