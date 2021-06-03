from django.contrib import admin
from django.urls import path, include
from blockchain import views
from blockchain.views import newBlockChain


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('get_chain', views.get_chain, name='get_chain'),
    path('get_transactions', views.get_chain, name='get_chain'),
    path('mine_block', views.mine_block, name='mine_block'),
    path('is_valid', views.is_valid, name='is_valid'),
    path('add_transaction', views.add_transaction, name='add_transaction'),
    path('connect_nodes', views.connect_node, name='connect_nodes'),
    path('replace_chain', views.replace_chain, name='replace_chain')
]
