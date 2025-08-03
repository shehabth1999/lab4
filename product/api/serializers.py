from rest_framework import serializers
from product.models import Product, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class ProductSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Product
        fields = '__all__'


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("username or password is incorrect")
        return user
