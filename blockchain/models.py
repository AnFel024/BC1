from django.db import models

# Create your models here.
class blockChain(models.Model):
    hash_pointer = models.CharField(max_length=256, blank=True, null=False)
    id = models.CharField(max_length=256, blank=True, null=False, primary_key=True)
    Nonce = models.CharField(max_length=256, blank=True, null=False)
    timestamp = models.DateTimeField(blank=True, null=False)
    number_of_transactions = models.IntegerField(default=0, blank=True, null=False)
