from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def create_user(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie:movie-index')
    return render(request, 'registration/signup.html', context={'form': form})
