from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def login_page(request):
    return render(request, 'app/login.html')

def profile_page(request):
    return render(request, 'app/profile.html')

class ProtectedDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
            "message": "This is protected data accessed via JWT!"
        })
