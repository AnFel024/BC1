from django.urls import path
from api.views import blockChainList, blockChainDetail, blockChainCreate
from django.conf.urls import url

urlpatterns = [
    path('blockchain', blockChainList.as_view()),
    path('blockchain/<str:pk>', blockChainDetail.as_view()),
    path('blockchain_create', blockChainCreate.as_view()),
]
