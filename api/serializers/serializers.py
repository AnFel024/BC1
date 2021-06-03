from django.db.models import fields
from blockchain.models import block, transaction

from rest_framework import serializers

class blockChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = block
        fields = ('hash_pointer','id','Nonce','timestamp','number_of_transactions')

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = ('sender','receiver','timestamp','amount','block_position')