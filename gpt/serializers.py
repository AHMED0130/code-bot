from rest_framework import serializers
from .models import Code

class CodeSerializer(serializers.ModelSerializer):
    solution=serializers.CharField(read_only=True)
    class Meta:
        model=Code
        fields=['problem','solution','language']
