from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated , AllowAny
from app.models import House
from app.serializers_f.arena_serializer import HouseSerializer
from rest_framework import status
from app.models.owner import Owner
from rest_framework import generics



class HouseCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = HouseSerializer

    def post(self, request):
        owner = request.data.get('owner')
        try:
            owner_user = Owner.object.get(pk=owner)
        except Owner.DoesNotExist:
            return Response({"error":"User does not exist"},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        if owner_user.house_count > 1:
            return Response({"limit":"adding house is limited!, please buy premium"})
        serializer = HouseSerializer(data=request.data)
        if serializer.is_valid():
            house = serializer.save()
            house.owner.house_count += 1
            house.owner.save()
            return Response(HouseSerializer(house).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # else:
    #     return Response({"error": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)


# {
# "name":"arena2",
# "location":"name",
# "owner":2,
# "cost":"1020",
# "open_time":"10:10",
# "close_time":"20:20"
# }


class HouseListView(APIView):
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    serializer_class = HouseSerializer
    def get(self, request, pk):
        try:
            # owner = request.user
            # house = House.objects.all()
            # house = House.objects.filter(owner=owner)
            house = House.objects.get(pk=pk)
        except House.DoesNotExist:
            return Response({"error": "House not found"}, status=status.HTTP_404_NOT_FOUND)
        # except Exception as e:
        serializer = HouseSerializer(house, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            house = House.objects.get(pk=pk)
            serializer = HouseSerializer(house, data=request.data, partial=True)
            if serializer.is_valid():
                house = serializer.save()
                return Response(HouseSerializer(house).data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except House.DoesNotExist:
            return Response({"error": "Arena not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            house = House.objects.get(pk=pk)
            house.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except House.DoesNotExist:
            return Response({"error": "House not found"}, status=status.HTTP_404_NOT_FOUND)