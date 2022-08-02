from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics
from core.models import Store, Que
from core.serializer import StoreSerializer, QueSerializer, QueListSerializer, MyQueSerializer
# Create your views here.

class StoreList(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class QueAPI(generics.CreateAPIView, generics.ListAPIView):
    queryset = Que.objects.all()
    serializer_class = QueSerializer


class MyQue(generics.ListAPIView):
    # serializer_class = MyQueSerializer

    def get(self, request):
        queues_count = Que.objects.all().count()
        return JsonResponse({'queue': queues_count})
