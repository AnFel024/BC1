from django.http import Http404
from django.db.models import Q  

from api.serializers.serializers import blockChainSerializer, transactionSerializer
from blockchain.models import block, transaction
from blockchain.views import newBlockChain

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class blockChainList(APIView):
    def get(self, request, format=None):
        print('pk')
        blockChainObject = block.objects.all()
        serializer = blockChainSerializer(blockChainObject, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = blockChainSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class blockChainCreate(APIView):
    def post(self, request, format=None):
        blockChainObject = block(hash_pointer='1', id='hash23', Nonce='23', timestamp='2021-03-18T13:50:20+00:00', number_of_transactions='234')
        serializer = blockChainSerializer(blockChainObject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class blockChainDetail(APIView):
    def get_object(self, pk):
        try:
            return block.objects.get(pk=pk)
        except block.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        blockChainObject = self.get_object(pk)
        serializer = blockChainSerializer(blockChainObject)
        return Response(serializer.data)

    def patch(self, request, pk, format=None):
        blockChainObject = self.get_object(pk)
        serializer = blockChainSerializer(blockChainObject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        blockChainObject = self.get_object(pk)
        serializer = blockChainSerializer(blockChainObject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        blockChainObject = self.get_object(pk)
        blockChainObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TransactionDetail(APIView):
    def get(self, request, format=None):
        mTransactionts = transaction.objects.all()
        print(len(mTransactionts))
        serializer = transactionSerializer(mTransactionts, many=True)

        return Response(serializer.data)
