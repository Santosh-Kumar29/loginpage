from django.db import models
from django.db import connection

# Create your models here.

class login_page(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(null=False, max_length=20)
    password = models.CharField(null=False, max_length=20)
    email_id = models.EmailField(null=False, max_length=50)
    mobile_no = models.CharField(null=False, max_length=15)
    is_active = models.BooleanField(null=False)

def __str__(self):
    return self.id + " " + self.username + " " + self.password + " " + self.email_id + " " + self.mobile_no + " " + self.is_active


