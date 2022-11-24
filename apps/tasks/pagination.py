from rest_framework import pagination

class TaskPagination(pagination.PageNumberPagination):
    """Task list pagination"""
    page_size = 25
    page_size_query_param = 'size'
    page_query_param = 'page'
    max_page_size = 100
