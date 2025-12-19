from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from .serializers import UserSerializerV1

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializerV1(users, many=True)
        
        # We assume request.version is populated by DRF versioning, 
        # but if not we can return 'v1' explicitly or still use request.version if available.
        # Given the original code used request.version, we'll try to use it, 
        # but since we are now in explicit v1 view, we can also default to 'v1' if needed.
        # However, for consistency with original behavior, I'll use request.version if it was key.
        # Actually, separate views allows us to remove the conditional logic.
        
        version = request.version if hasattr(request, 'version') and request.version else 'v1'

        return Response({
            "version": version,
            "count": users.count(),
            "data": serializer.data
        })
