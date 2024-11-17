
from django.db import models
from main.models.autors import Autors


class Books(models.Model):
    id = models.AutoField(primary_key=True, db_index=True, unique=True)
    title = models.CharField(max_length=225, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    publish_date = models.DateField(blank=False, null=True)
    author_id = models.ForeignKey(
        Autors, related_name='autors', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        title = self.title
        return '{}'.format(title)

    class Meta:
        db_table = 'books'
        verbose_name_plural = 'Books'
