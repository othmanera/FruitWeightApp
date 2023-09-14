
from django.db import models
from django.contrib.auth.models import User

#
class droppedFile(models.Model):
    name = models.CharField(max_length=30)
    file = models.FileField(upload_to='FruitWeightWebApp/dropped_files/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class fileHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    droppedFile = models.ForeignKey(droppedFile, on_delete=models.CASCADE)

    def __str__(self):
        return f"user : {self.user} | quiz: {self.droppedFile}"