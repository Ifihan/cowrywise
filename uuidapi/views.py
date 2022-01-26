from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UUID
from .serializers import UUIDSerializer


class GetUUID(APIView):
    serializers = UUIDSerializer

    # def get(self, request):
    #     instance = UUID.objects.create()
    #     instance.save()

    #     data = UUID.objects.order_by('-timestamp')
    #     response = {}
    #     for item in data:
    #         response = {'timestamp': item.timestamp, 'id': item._id}
    #     return Response(response, status=200)

    def get(self, request):
        UUID.objects.create()
        prev_uuid = UUID.objects.order_by('-timestamp')
        ser_uuid = self.serializers(prev_uuid, many=True)

        data = ser_uuid.data
        return Response(data, status=200)


