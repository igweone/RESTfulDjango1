from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status

from .serializers import HelloSerializer


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView Features"""
        an_apiview = [
            'Uses Http methods as functions(get,post,patch,put, delte)',
            'it is cool',
            'i like it'
        ]
        return Response({'message':'hello', 'an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name """
        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        """Handles updating a specific object"""

        return Response({'method':'put'})

    
    def patch(self, request, pk=None):
        """Patch request only updates fields provided in the request"""

        return Response({'method':'patch'})

    
    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method':'delete'})

