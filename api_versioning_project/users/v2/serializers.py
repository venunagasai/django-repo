from rest_framework import serializers
from users.models import User

class UserSerializerV2(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age', 'status']

    def get_status(self, obj):
        return "ACTIVE" if obj.is_active else "INACTIVE"
