from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response

from api.serializers import ProfileSerializer
from users.models import Profile


class SignInAPIView(generics.GenericAPIView):
    serializer_class = ProfileSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        if not profile:
            profile = Profile.objects.create(user=user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)


class SubscriptionUpdate(generics.GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        profile = request.user.profile
        serializer = self.get_serializer(profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
