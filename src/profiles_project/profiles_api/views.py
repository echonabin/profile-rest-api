from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

# Create your views here.
class HelloApiView(APIView):
    """ Test API """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ API view features """
        an_APIview = [
            'just an api view with i dont understand a single freaking thing!'
            'i guess this is just a causual text rather than a code'
        ]

        return Response({'message' : 'Hi!', 'apiview' : an_APIview})

    def post(self, request):

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)