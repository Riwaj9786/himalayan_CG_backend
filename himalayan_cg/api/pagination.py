from rest_framework import pagination

class BlogLimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 3