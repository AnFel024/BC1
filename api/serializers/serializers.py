from django.db.models import fields
from blockchain.models import blockChain

from rest_framework import serializers

class blockChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = blockChain
        fields = ('hash_pointer','id','Nonce','timestamp','number_of_transactions')