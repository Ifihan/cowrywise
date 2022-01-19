from django.db import models
import uuid

def hex_uuid():
    return uuid.uuid4().hex

class Data(models.Model):
    _id = models.UUIDField(primary_key=True, default=hex_uuid, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return the timestamp and id together in a dictionary
        return {self.timestamp, self._id}
