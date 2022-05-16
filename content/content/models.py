from django.db import models
from core.base_model import BaseModel

class Content(BaseModel):
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    catalog_id  = models.IntegerField(default=0)
