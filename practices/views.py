from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render
from .models import Practice

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'practices': Practice.objects.all()
    })

def about(request):
    return render(request, 'about.html')

class CreatePractice(CreateView):
    model = Practice
    fields = ['description']
    success_url = '/'

class UpdatePractice(UpdateView):
    model = Practice
    fields = ['description', 'completed']
    success_url = '/'

class DeletePractice(DeleteView):
    model = Practice
    success_url = '/'

