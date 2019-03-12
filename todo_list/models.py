from django.db import models

# Create your models here.

class list(models.Model):
    item=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    def __str__(self):
        return self.item + ' | ' + str(self.completed)
class mail_id(models.Model): 
    mail=models.CharField(max_length=30,primary_key=True)

    
