from rest_framework import serializers

from core.models import User


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    class Meta:
        model = User
        fields = ('email', 'name', 'is_active', 'user_type')
        read_only_fields = ('email', 'id')