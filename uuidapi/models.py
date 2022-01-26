from django.db import models
import uuid

def hex_uuid():
    return uuid.uuid4().hex

class UUID(models.Model):
    _id = models.UUIDField(primary_key=True, default=hex_uuid, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return f"{self.timestamp} : {self._id}"
