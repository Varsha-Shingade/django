from django.db import models


# Create your models here.
class Feedback(models.Model):
    name=models.CharField((""), max_length=50)
    email=models.EmailField((""), max_length=254)
    pno=models.CharField((""), max_length=50)
    desc=models.CharField((""), max_length=500)
    def __str__(self):
        return self.name
    
