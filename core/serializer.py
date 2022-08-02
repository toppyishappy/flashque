from rest_framework import serializers
from core.models import Store, Que


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'



class QueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Que
        exclude = ['status']

class QueListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Que
        fields = '__all__'


class MyQueSerializer(serializers.Serializer):
    que = serializers.CharField()