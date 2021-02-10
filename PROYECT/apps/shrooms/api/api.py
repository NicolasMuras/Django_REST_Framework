from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.shrooms.models import Shroom
from apps.shrooms.api.serializers import ShroomSerializer
from apps.shrooms.api.serializers import DetailShroomSerializer
from apps.shrooms.api.serializers import CreateShroomSerializer
from apps.shrooms.api.serializers import UpdateShroomSerializer

@api_view(['GET', 'POST'])
def shroom_api_view(request):

    # List all shrooms
    if request.method == 'GET':
        shrooms = Shroom.objects.all().values('id', 'specie', 'days', 'cap_color', 'trunk_color')
        shroom_serializer = ShroomSerializer(shrooms, many = True)
        return Response(shroom_serializer.data, status = status.HTTP_200_OK)

    # Create
    elif request.method == 'POST':
        shroom_serializer = ShroomSerializer(data = request.data)

        # Validation
        if shroom_serializer.is_valid():
            shroom_serializer.save()
            return Response({'message':'Specimen was created successfull !'}, status = status.HTTP_200_OK)

        return Response(shroom_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def shroom_detail_api_view(request, pk=None):
    # Queryset
    shroom = Shroom.objects.filter(id = pk).first()

    # Validation
    if shroom:
        
        # Retrieve
        if request.method == 'GET':
            shroom_serializer = DetailShroomSerializer(shroom)
            return Response(shroom_serializer.data, status = status.HTTP_200_OK)

        # Update
        elif request.method == 'PUT':
            shroom_serializer = UpdateShroomSerializer(shroom, data = request.data)
            if shroom_serializer.is_valid():
                shroom_serializer.save()
                return Response(shroom_serializer.data, status = status.HTTP_200_OK)
            return Response(shroom_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        # Delete
        elif request.method == 'DELETE':
            shroom.delete()
            return Response({'message':'The shroom was successfull deleted'}, status = status.HTTP_200_OK)

    return Response({'message':'Shroom not found'}, status = status.HTTP_400_BAD_REQUEST)