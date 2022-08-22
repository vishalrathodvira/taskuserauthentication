from django.db import models

# Create your models here.
class employee(models.Model):
    bio=models.CharField(max_length=100)
    img=models.ImageField(null=True,blank=True,upload_to="images/")
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    number=models.IntegerField()
    dob=models.DateField()
    email=models.EmailField()
    country=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    dist=models.CharField(max_length=100)
    edu=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    year=models.IntegerField()
    mark=models.IntegerField()
    role=models.CharField(max_length=100)
    duration=models.DateField()
    sal=models.IntegerField()
    

    def __str__(self):
        return self.fname,self.lname