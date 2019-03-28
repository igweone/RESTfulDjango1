from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets


from .serializers import HelloSerializer
from .serializers import UserProfileSerializer

from .models import UserProfile
from .permissions import UpdateOwnProfile



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


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = HelloSerializer


    def list(self, request):
        """Return a hello message"""
        a_viewsets = [
            'Uses actions (List, create, retrieve, update, partial_update',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code'
        ]
        return Response({"message":"hello", "a_viewset":a_viewsets})

    def create(self, request):
        """create a new hello message"""
        serializer = HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = "Hello {0}".format(name)
            return Response({"message":message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def retrieve(self, request, pk=None):
        """Handles getting a specific object by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handles updating a specific object by its ID"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handles updating part of a specific object by its ID"""
        return Response({'http_method':'PATCH'})

    def destroy (self, request, pk=None):
        """Handles removing a specific object by its ID"""
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """handles creating, and updating profiles"""
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)




