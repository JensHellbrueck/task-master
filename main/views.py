from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage

class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        # Überprüfe, ob die Datei im Request enthalten ist
        file = request.FILES.get('file')
        #FILES.get
        if not file:
            return Response({"message": "Keine Datei zum Hochladen gefunden"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Speichere die Datei
        file_name = default_storage.save(file.name, file)
        file_url = default_storage.url(file_name)
        
        return Response({"url": file_url}, status=status.HTTP_201_CREATED)

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