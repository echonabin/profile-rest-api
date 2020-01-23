from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """ Test API """
    def get(self, request, format=None):
        """ API view features """
        an_APIview = [
            'just an api view with i dont understand a single freaking thing!'
            'i guess this is just a causual text rather than a code'
        ]

        return Response({'message' : 'Hi!', 'apiview' : an_APIview})