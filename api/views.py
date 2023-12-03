from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
# Create your views here.
from rest_framework import viewsets


@api_view(['GET'])
def get_routs(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def note_list(request):
    if request.method == 'GET':
        notes = Note.objects.all().order_by('-updated')
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_note(request, pk):
    try:
        note = Note.objects.get(id=pk)
    except:
        raise Note.DoesNotExist
    if request.method == 'GET':
        serializer = NoteSerializer(note)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    if request.method == 'PUT':
        serializer = NoteSerializer(instance=note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        note.delete()

# @api_view(['GET', 'PUT'])
# def update_note(request, pk):
#     try:
#         note = Note.objects.get(id=pk)
#     except:
#         raise Note.DoesNotExist
#     if request.method == 'GET':
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = NoteSerializer(instance=note, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


# @api_view(['GET', 'DELETE'])
# def delete_note(request, pk):
#     try:
#         note = Note.objects.get(id=pk)
#     except:
#         raise Note.DoesNotExist
#     if request.method == 'GET':
#         serializer = NoteSerializer(note)
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         note.delete()
#         return Response(status=status.HTTP_200_OK)


# @api_view(['POST', 'GET'])
# def create_note(request):
#     if request.method == 'GET':
#         note = Note.objects.all()
#         serializer = NoteSerializer(note, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         # note = Note.objects.create(
#         #     note=request.data['note']
#         # )
#         # print(note)
#         serializer = NoteSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
