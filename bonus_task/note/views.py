from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note

class NoteListView(ListView):
    model = Note
    template_name = 'note/note_list.html'
    context_object_name = 'notes'

class NoteDetailView(DetailView):
    model = Note
    template_name = 'note/note_detail.html'

class NoteCreateView(CreateView):
    model = Note
    template_name = 'note/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('note_list')

class NoteUpdateView(UpdateView):
    model = Note
    template_name = 'note/note_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('note_list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note/note_confirm_delete.html'
    success_url = reverse_lazy('note_list')
