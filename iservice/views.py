from . import models

from rest_framework.response import Response

from rest_framework import status

from . import serializers

from rest_framework.views import APIView


class UserAPIView(APIView):

    def get(self,resquest,*args,**kwargs):
        return Response('Hello, World!', status=status.HTTP_201_CREATED)
    #def post(self,resquest,*args,**kwargs):
    #def delet(self,resquest,*args,**kwargs):
    #def put(self,resquest,*args,**kwargs):