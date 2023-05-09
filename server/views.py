from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .logic import matching_algo
from .get import *



@api_view(['POST'])
def listen(request):

    if request.method == 'POST':
        deserialized = String_(data=request.data)
        
        if deserialized.is_valid():
            likes = deserialized.data['argument_1']
            answer = matching_algo(likes)

            return Response(answer, status=status.HTTP_200_OK)

        else:
            return Response(deserialized.errors)



@api_view(['GET'])
def get_food(request):

    if request.method == 'GET':
        deserialized = String_(data=request.data)
        
        answer = food()

        return Response(answer, status=status.HTTP_200_OK, headers={'Content-Type': 'application/json'})


@api_view(['GET'])
def get_entertainment(request):

    if request.method == 'GET':
        deserialized = String_(data=request.data)
        
        answer = entertainment()

        return Response(answer, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cultural(request):

    if request.method == 'GET':
        deserialized = String_(data=request.data)
        
        answer = cultural()

        return Response(answer, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_outdoor(request):

    if request.method == 'GET':
        deserialized = String_(data=request.data)
        
        answer = outdoor()

        return Response(answer, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_trips(request):

    if request.method == 'GET':
        deserialized = String_(data=request.data)
        
        answer = trips()
        return Response(answer, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_drunk(request):

    if request.method == 'GET':
        deserialized = String_(data=request.data)
        
        answer = drunk()

        return Response(answer, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_student(request):

    if request.method == 'GET':
        deserialized = String_(data=request.data)
        
        answer = student()

        return Response(answer, status=status.HTTP_200_OK)
        

@api_view(['GET'])
def get_friends(request):

    if request.method == 'GET':
        deserialized = String_(data=request.data)
        
        answer = friends()

        return Response(answer, status=status.HTTP_200_OK)



@api_view(['GET'])
def get_family(request):

    if request.method == 'GET':
        deserialized = String_(data=request.data)
        
        answer = family()

        return Response(answer, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_couples(request):

    if request.method == 'GET':
        deserialized = String_(data=request.data)
        
        answer = couples()

        return Response(answer, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_tourists(request):

    if request.method == 'GET':
        deserialized = String_(data=request.data)
        
        answer = tourists()

        return Response(answer, status=status.HTTP_200_OK)