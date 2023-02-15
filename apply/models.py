from django.db import models

# Create your models here.
class Apply(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    EmailAddress = models.CharField(max_length=55)
    City = models.CharField(max_length=25)
    Country = models.CharField(max_length=25)

    def __str__(self):
        return f"Apply(FirstName: {self.FirstName}, LastName: {self.LastName}, Email: {self.EmailAddress})"
        #this is dunder method it manage how your db data will be displayed
       