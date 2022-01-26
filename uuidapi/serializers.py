from rest_framework import serializers
from .models import UUID
from collections import OrderedDict
from functools import reduce

class UUIDSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S.%f")

    class Meta:
        model = UUID
        fields = ('timestamp', '_id')

    def represent(self, generator):
        new_id = OrderedDict()
        new_id[str(generator.timestamp).split('+')[0]] = generator.uuid
        return new_id

    