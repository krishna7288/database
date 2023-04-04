from msilib import Table
from rest_framework import serializers 

 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Table
        fields = ["title","description","published"]


