from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NoteSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Notes
from .utils import *
# Create your views here.
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        print(type(user))
        print(type(user.username))
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):

    return Response('Welcome Django')

@csrf_exempt
@api_view(['GET','POST'])
def getNotes(request):

    if request.method=='GET':
        data = getNoteList(request)
        return Response(data)

    elif request.method=='POST':
        data = postNote(request)
        return Response(data)


@api_view(['GET','PUT','DELETE'])
def getNote(request,pk):
    if request.method=='GET':
        data = getOneNote(request,pk)
        return Response(data)

    elif request.method=='PUT':
        data = updateNote(request,pk)
        return Response(data)

    elif request.method=='DELETE':
        deleteNote(request,pk)
        response = Response("Note was deleted!")
        return response


    