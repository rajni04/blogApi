from django.db import models
from django.conf import settings





# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    image=models.ImageField(blank=True,null=True)
    content=models.TextField()
    publish=models.DateField(auto_now=False,auto_now_add=False)
    updated=models.DateField(auto_now=True,auto_now_add=False)

   