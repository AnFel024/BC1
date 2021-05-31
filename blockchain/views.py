from re import T
from urllib import parse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpRequest, response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import request, status
import rest_framework

from blockchain.models import blockChain

import datetime
import hashlib
import json
import socket

from uuid import uuid4
from urllib.parse import urlparse

class newBlockChain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.nodes = set()
        self.new_block(nonce=1, hash_pointer='0')

    def new_block(self, nonce, hash_pointer):
        block = {
            'index': len(self.chain) + 1, 
            'timestamp': str(datetime.datetime.now()),
            'nonce': nonce,
            'hash_pointer': hash_pointer,
            'transactions': self.transactions
            }
        self.transactions = []
        self.chain.append(block)

        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_nonce):
        new_nonce = 1
        check_nonce = False
        while check_nonce is False:
            hash_operation = hashlib.sha256(str(new_nonce**2 - previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_nonce = True
            
            else:
                new_nonce += 1
        
        return new_nonce
    
    #TODO Revisar la razon de esta funcion
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        
        while block_index < len (chain):
            block = chain[block_index]
            if block['hash_pointer'] != self.hash(previous_block):
                return False
            previous_nonce = previous_block['nonce']
            nonce = block['nonce']
            hash_operation = hashlib.sha256(str(nonce**2 -previous_nonce**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        
        return True
    
    #TODO Quitar str de time
    def add_transaction(self, sender, receiver, amount, time):
        self.transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'time': str(datetime.datetime.now())
        })
        previus_block = self.get_previous_block()
        return previus_block['index'] + 1

    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)

        for node in network:
            response = request.get(f'http:{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        
        if longest_chain:
            self.chain = longest_chain
            return True
        return False

blockchain = newBlockChain()
node_address = str(uuid4()).replace('-','')
root_node = 'e36f0158f0aed45b3bc755dc52ed4560d'


def mine_block(request):
    if request.method == 'GET':
        previous_block = blockchain.get_previous_block()
        print(previous_block)
        previous_nonce = previous_block['nonce']
        nonce = blockchain.proof_of_work(previous_nonce)
        hash_pointer = blockchain.hash(previous_block)
        block = blockchain.new_block(nonce, hash_pointer)

        response = {
            'message':'Bloque creado!',
            'index':block['index'],
            'timestamp': block['timestamp'],
            'nonce':block['nonce'],
            'hash_pointer':block['hash_pointer']
        }

    return JsonResponse(response)

def get_chain(request):
    if request.method == 'GET':
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain)
        }

    return JsonResponse(response)

def is_valid(request):
    if request.method == 'GET':
        is_valid = blockchain.is_chain_valid(blockchain.chain)
        if is_valid:
            response = {
                'message':'El bloque es valido!'
            }
        else:
            response = {
                'message':'El bloque esta corrupto!'
            }
        
    return JsonResponse(response)

@csrf_exempt
def add_transaction(request):
    if request.method == 'POST':
        print(request.body)
        received_json = json.loads(request.body)
        transaction_keys = ['sender', 'receiver', 'amount', 'time']

        if not all(key in received_json for key in transaction_keys):
            return HttpResponse(status=400)
        
        index = blockchain.add_transaction(received_json['sender'], received_json['receiver'], received_json['amount'],received_json['time'])
        response = {
            'message': f'Transacción agregada al bloque {index}',
        }

    return JsonResponse(response)

@csrf_exempt
def connect_node(request):
    if request.method == 'POST':
        print(type(request.body))
        received_json = json.loads(request.body)
        nodes = received_json.get('nodes')
        
        if nodes is None:
            return 'No hay nodos en lista', HttpResponse(status=400)

        for node in nodes:
            blockchain.add_node(node)
        
        response = {
            'message': 'Los siguientes nodos se encuentran conectados:',
            'total_nodes': list(blockchain.nodes),
        }

    return JsonResponse(response)

def replace_chain(request):
    if request.method == 'GET':
        is_chain_replaced = blockchain.replace_chain()
        if is_chain_replaced:
            response = {
                'message': 'los nodos tuvieron diferentes cadenas y fueron reemplazadas',
                'new_chain':blockchain.chain
            }
        
        else:
            response = {
                'message': 'Las cadenas se encuentran en armonia con el ambiente.',
                'actual_chain': blockchain.chain
            }

    return JsonResponse(response)