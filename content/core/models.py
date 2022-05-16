from django.db import models
from core.utils import generate_pk

class BaseModel(models.Model):
    id = models.CharField(primary_key=True, max_length=255, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            id_prefix = getattr(self, "id_prefix")
            if id_prefix is not None:
                setattr(self, 'id', generate_pk(self.id_prefix))
        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Content(BaseModel):
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    catalog_id  = models.IntegerField(default=0)
