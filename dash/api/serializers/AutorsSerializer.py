# serializers.py
from api.serializers.BooksSerializer import BooksSerializer
from main.models import Autors, Books
from rest_framework import serializers


class AutorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autors
        fields = '__all__'


class AutorsRelationSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    def get_books(self, obj):
        books = Books.objects.filter(author_id=obj)
        if books:
            serializer = BooksSerializer(books, many=True).data
            return serializer
        return None

    class Meta:
        model = Autors
        fields = '__all__'
