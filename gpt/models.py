from django.db import models
from django.conf import settings
# Create your models here.

class Code(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    problem=models.TextField()
    language=models.CharField(max_length=50)
    solution=models.TextField()


