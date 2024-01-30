from rest_framework import serializers
from books.models import Book
from django.contrib.auth.models import User
class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','title','author','price']

class userserilizer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password']

    def create(self, validated_data):
            u = User.objects.create(username=validated_data['username'])
            u.set_password(validated_data['password'])
            u.save()
            return u