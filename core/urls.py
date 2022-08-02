from django.urls import path

from core.views import StoreList, QueAPI, MyQue

urlpatterns = [
    path('store/', StoreList.as_view()),
    path('que/', QueAPI.as_view()),
    path('me/', MyQue.as_view()),
]