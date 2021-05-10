from rest_framework import serializers, viewsets, status
from .models import Single
from .serializers import SingleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class SingleViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def single_list(self, format=None):
        single = Single.objects.all()
        single_serializer = SingleSerializer(single, many=True)
        return Response(single_serializer.data)

    @api_view(['POST'])
    def create(self, format=None):
        single_serializer = SingleSerializer(data=self.data)
        if single_serializer.is_valid():
            single_serializer.save()
            return Response(single_serializer.data, status=status.HTTP_201_CREATED)
        return Response(single_serializer.errors, status=status.HTTP_400_BAD_REQUEST)