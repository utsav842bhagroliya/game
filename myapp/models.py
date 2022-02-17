from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=15,unique=True)
    ver_code = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)
    invite_code = models.CharField(max_length=20)
    bank_account = models.CharField(max_length=30,null=True)
    ifsc_code = models.CharField(max_length=20,null=True)
    rechage = models.IntegerField(default=0)


    def __str__(self):
        return self.mobile