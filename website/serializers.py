from django.contrib.auth.models import User, Group
from book.models import Book, BookMain, BookDetail
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class BookMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMain
        fields = ['id','title','author']

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetail
        fields = [field.name for field in BookDetail._meta.get_fields()]

class BookSerializer(serializers.ModelSerializer):
    main = BookMainSerializer(read_only=True)
    detail = BookDetailSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['id','main','detail']