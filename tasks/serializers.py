from rest_framework import serializers
from tasks.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=50)
    
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'created_at', 'updated_at']
