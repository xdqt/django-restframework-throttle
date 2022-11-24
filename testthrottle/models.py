from django.db import models

class EllisTest(models.Model):
    username = models.BigAutoField(primary_key=True,null=False,blank=False)
    address = models.CharField(max_length=100,null=False,blank=False)
    class Meta:
        db_table="ellistest"

# Create your models here.
