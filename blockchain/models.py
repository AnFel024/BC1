from django.db import models

# Create your models here.
class block(models.Model):

    class Meta:
        db_table= 'block'

    hash_pointer = models.CharField(max_length=256, blank=True, null=False)
    id = models.CharField(max_length=256, blank=True, null=False, primary_key=True)
    Nonce = models.CharField(max_length=256, blank=True, null=False)
    timestamp = models.DateTimeField(blank=True, null=False)
    number_of_transactions = models.IntegerField(default=0, blank=True, null=False)
    index = models.IntegerField(default=0, blank=True, null=False)

class transaction(models.Model):

    class Meta:
        db_table= 'transaction'

    sender = models.CharField(max_length=256, blank=True, null=False)
    receiver = models.CharField(max_length=256, blank=True, null=False)
    timestamp = models.DateTimeField(blank=True, null=False)
    amount = models.IntegerField(default=0, blank=True, null=False)
    block_position = models.CharField(max_length=256, blank=True, null=False)