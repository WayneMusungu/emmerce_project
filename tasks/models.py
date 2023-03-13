from django.db import models
from accounts.models import User

class Todo(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todos")
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-created_at"]
    
   
