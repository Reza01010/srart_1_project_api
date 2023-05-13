from rest_framework import permissions, authentication, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from .models import Item, Jonyur,JonyurUser
from .serializers import ItemSerializer, JonyurSerializer, JonyurUserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


@api_view(['GET'])
def jonyur_view(request):
    queryset = Jonyur.objects.all()
    serializer = JonyurSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def jonyur_user_view(request):
    if request.method == 'GET':
        queryset = JonyurUser.objects.all()
        serializer = JonyurUserSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = JonyurUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
