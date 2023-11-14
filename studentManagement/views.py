from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from studentManagement.models import Student


def list_view(request):
    items = Student.objects.all()
    return render(request, 'list.html', {'items': items})

class StudentCreate(CreateView):
    model = Student
    template_name = 'form.html'
    fields = ('nome', 'matricula', 'email', 'serie', 'curso', 'idade', 'conclusao')
    success_url = reverse_lazy('student-list')