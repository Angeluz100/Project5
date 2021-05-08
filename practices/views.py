from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Practice

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        practices = Practice.objects.filter(user=request.user)
    else:
        practices = None
    return render(request, 'index.html', {
        'practices': practices
    })

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        # else:
        #     return redirect('signup')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


class CreatePractice(CreateView, LoginRequiredMixin):
    model = Practice
    fields = ['description']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdatePractice(UpdateView, LoginRequiredMixin):
    model = Practice
    fields = ['description', 'completed']
    success_url = '/'

class DeletePractice(DeleteView, LoginRequiredMixin):
    model = Practice
    success_url = '/'

