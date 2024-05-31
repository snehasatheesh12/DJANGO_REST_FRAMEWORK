from . models import *
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['id','name','roll','city']