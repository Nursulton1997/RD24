import json

from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta
from .serializer import UserSerializer


# Create your views here.


class LastUserHundred(APIView):
    def get(self, request):
        last30 = timezone.now() - timedelta(days=30)
        top_user = (User.objects.filter(reports__created_at__gte=last30)).annotate(count=Count('reports')).order_by(
            '-count')[:100].select_related('oneid')

        serializer = UserSerializer(top_user, many=True)
        return Response(serializer.data, 200)
