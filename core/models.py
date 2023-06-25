from django.db import models
from django.contrib.auth.models import User

DES = (
    ('PATIENT','PATIENT'),
    ('DOCTOR','DOCTOR'),
)
LEVEL = (
    ("NONE","NONE"),
    ("LOW","LOW"),
    ("MEDIUM","MEDIUM"),
    ("HIGH","HIGH")
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    desg = models.CharField(max_length=255,choices=DES)
    number = models.CharField(max_length=12)
    

class Vitals(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    doctor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='doctor',blank=True)
    bt = models.FloatField()
    spo2 = models.IntegerField()
    pr = models.IntegerField()
    bp = models.IntegerField()
    cm = models.IntegerField()
    cl = models.CharField(max_length=50,choices=LEVEL)

    def __str__(self) -> str:
        return self.user.username + str(self.cl)
    
    timestramp = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-id']