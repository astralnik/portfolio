from django.shortcuts import render

from .models import Note

# Create your views here.

def note_list(request):
    notes = Note.objects.order_by('published_date')     # Список заметок по дате (сперва первые)
    return render(request, 'notebook/note_list.html', {'notes':notes})


