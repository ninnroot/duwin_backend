from django.db import models


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now=True,
                                      help_text="Creation datetime of this object.")
    updated_at = models.DateTimeField(auto_now_add=True,
                                      help_text="Last edited datetime of this object.")

    class Meta:
        abstract = True

