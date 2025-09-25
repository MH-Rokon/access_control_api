from django.db import models




# Model for logging access conrol 
class AccessLog(models.Model):
    card_id = models.CharField(max_length=50)          
    door_name = models.CharField(max_length=100)       
    access_granted = models.BooleanField()             
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.card_id
