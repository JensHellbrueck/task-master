from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(
    [
        "POST",
    ]
)
def register(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    email = request.POST.get("email", None)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Username already exists"})
    if not username or not password or not email:
        return JsonResponse({"error": "Missing required fields"})

    try:
        User.objects.create_user(username, email, password)
        return JsonResponse({"success": "User created"})
    except Exception as e:
        return JsonResponse({"error": str(e)})