from django.db import models

class Interaction(models.Model):
    
    
    sender = models.CharField(max_length=256)
    recipient = models.CharField(max_length=256)
    message = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    