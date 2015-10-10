from django.db import models

class TransactionRecordElement(models.Model):

    TYPE_CHOICES = (
        ('da', 'transaction date'),
        ('tt', 'transaction type'),
        ('na', 'name'),
        ('na', 'memo'),
        ('tr', 'transaction amount'),
    )

    name = models.CharField(max_length=256, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    element_type = models.CharField(null=True, blank=True, max_length=2, choices=TYPE_CHOICES)
    date_format = models.CharField(max_length=256, null=True, blank=True)
    active = models.BooleanField(default=True)
