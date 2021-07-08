from rest_framework import serializers

from users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(source='user.username')

    class Meta:
        model = Profile
        fields = '__all__'
