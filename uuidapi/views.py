from venv import create
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Data
from .serializers import DataSerializer


class GetUUID(APIView):
    serializers = DataSerializer

    def get(self, request):
        instance = Data.objects.create()
        instance.save()

        data = Data.objects.order_by('-timestamp')
        response = {}
        for item in data:
            response = {'timestamp': item.timestamp, 'id': item._id}
        return Response(response, status=200)
