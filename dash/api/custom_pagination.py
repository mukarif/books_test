import math
from urllib import parse

from django.conf import settings
from django.utils.encoding import force_str
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class NotFound(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = ('bad_request.')
    default_code = 'bad_request'


class NotFoundData(APIException):
    status_code = status.HTTP_200_OK
    default_detail = ('success.')
    default_code = 'success'


DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = settings.REST_FRAMEWORK['PAGE_SIZE']


class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE

    def get_paginated_response(self, data):
        # if you want to show page size in resposne just add these 2 lines
        if self.request.query_params.get('page_size'):
            self.page_size = int(self.request.query_params.get('page_size'))

        # you can count total page from request by total and page_size
        total_page = math.ceil(self.page.paginator.count /  # type: ignore
                               self.page_size)

        return Response({
            'count': self.page.paginator.count,  # type: ignore
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total_page': total_page,
            'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
            'page_size': int(self.request.GET.get('page_size', self.page_size)),
            'results': data
        })
