# views.py
from api.custom_pagination import CustomPagination
from api.serializers.BooksSerializer import BooksSerializer
from django.core.cache import cache
from main.models import Books
from rest_framework import filters, viewsets
from rest_framework.response import Response


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('title')
    serializer_class = BooksSerializer

    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)

    cache_key_prefix = "books"

    def paginate_queryset(self, queryset, view=None):
        """
        TURN OFF/ON PAGINATION IN MODELVIEWSET
        """
        if 'no_page' in self.request.query_params:
            return None
        else:
            return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def list(self, request, *args, **kwargs):
        cache_key = f"{self.cache_key_prefix}_list"
        cached_data = cache.get(cache_key)
        search = self.request.query_params.get('search')
        if search:
            cache.delete(cache_key)
        if cached_data:

            paginator = CustomPagination()
            paginator.page_size = 15
            pg = paginator.paginate_queryset(cached_data, request)

            data = paginator.get_paginated_response(pg)

            return data

        # Fetch from DB and serialize
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        cache.set(cache_key, serializer.data,
                  timeout=60 * 5)  # Cache for 5 minutes

        paginator = CustomPagination()
        paginator.page_size = 15
        pg = paginator.paginate_queryset(serializer.data, request)

        data = paginator.get_paginated_response(pg)

        return data

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        cache_key = f"{self.cache_key_prefix}_detail_{instance.id}"
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        serializer = self.get_serializer(instance)
        cache.set(cache_key, serializer.data, timeout=60 * 5)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Clear cache on creation
        cache.delete(f"{self.cache_key_prefix}_list")
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        instance = self.get_object()
        cache_key = f"{self.cache_key_prefix}_detail_{instance.id}"
        # Clear detail cache and list cache
        cache.delete(cache_key)
        cache.delete(f"{self.cache_key_prefix}_list")
        return response

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().destroy(request, *args, **kwargs)
        cache_key = f"{self.cache_key_prefix}_detail_{instance.id}"
        # Clear detail cache and list cache
        cache.delete(cache_key)
        cache.delete(f"{self.cache_key_prefix}_list")
        return response
