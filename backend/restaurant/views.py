from datetime import date

from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Menu
from .serializers import MenuSerializer, MealSerializer


class MenuAPIView(APIView):

    def get(self, request, format=None):
        menus = Menu.objects.filter(date=date.today())
        output = {
            "breakfast": MenuSerializer(menus.filter(day_period=1).first()).data,
            "lunch": MenuSerializer(menus.filter(day_period=2).first()).data,
            "dinner": MenuSerializer(menus.filter(day_period=3).first()).data
        }
        return Response(output, 200)
