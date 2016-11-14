from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Location
from .serializer import Converter
from rest_framework.response import Response
from rest_framework import status


# GET: FETCHES ALL DATA AND SHOWS IT
# POST: ADDS NEW DATA TO COLLECTION
@api_view(['GET','POST','PUT'])
def post_collection(request):

    if request.method == 'GET':
        coordinates= Location.objects.all()
        converter = Converter(coordinates, many=True)
        return Response(converter.data)
    if request.method == 'POST':
        converter = Converter(data=request.data)
        if converter.is_valid():
            converter.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(converter.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def post_element(request,pk):
    print("pk=" + pk)
    if request.method=='GET':
        try:
            element = Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        converter = Converter(element)
        return Response(converter.data)