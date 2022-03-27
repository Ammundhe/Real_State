from django.db import models

class realtor(models.Model):
    name=models.CharField(max_length=150)
    photo=models.ImageField()
    email=models.EmailField()
    description=models.TextField()
    phoneNumber=models.CharField(max_length=12)

    def __str__(self) -> str:
        return str(self.name)