from .serializers import NoteSerializer
from django.views.decorators.csrf import csrf_exempt
from .models import Notes

@csrf_exempt
def postNote(request):
    data = request.data
    note = Notes.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note,many=True)
    if serializer.is_valid:
        serializer.save()
    return serializer.data

@csrf_exempt
def getNoteList(request):
    notes = Notes.objects.all().order_by('-updated')
    serializer = NoteSerializer(notes,many=True)
    return serializer.data

@csrf_exempt
def deleteNote(request,pk):
    note = Notes.objects.get(id=pk)
    note.delete()

@csrf_exempt
def updateNote(request,pk):
    data =request.data
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(instance=note,data=data)

    if serializer.is_valid():
        serializer.save()
    return serializer.data


def getOneNote(request,pk):
    notes = Notes.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)
    return serializer.data













