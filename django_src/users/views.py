from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class WhoAmIView(APIView):
    """ Simple endpoint to test auth """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """ Return request.user and request.auth """
        return Response({
            'user': model_to_dict(request.user),
            'auth': request.auth
        })
