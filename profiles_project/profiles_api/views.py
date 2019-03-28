from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response


class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses Http methods as functions(get,post,patch,put, delte)',
            'it is cool',
            'i like it'
        ]
        return Response({'message':'hello', 'an_apiview':an_apiview})

