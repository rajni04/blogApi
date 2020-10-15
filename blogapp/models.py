from django.db import models
from django.contrib.auth.models import User





# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(blank=True,null=True)
    content=models.TextField()
    publish=models.DateField(auto_now=False,auto_now_add=False)
    updated=models.DateField(auto_now=True,auto_now_add=False)

   