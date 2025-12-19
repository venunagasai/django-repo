from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from .serializers import UserSerializerV2

class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializerV2(users, many=True)
         
        version = request.version if hasattr(request, 'version') and request.version else 'v2'

        return Response({
            "version": version,
            "count": users.count(),
            "data": serializer.data
        })
