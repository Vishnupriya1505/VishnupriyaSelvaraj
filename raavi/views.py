from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class betacls(APIView):
    def post(self):
        return Response("HEYY BUDDY")
        
