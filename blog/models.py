from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True)
    description = models.CharField('Description',
                                   max_length=100, blank=True,
                                   help_text='simple description')
    create_date = models.DateTimeField('Date Created', auto_now_add=True,
                                       blank=True, null=True)
    modify_date = models.DateTimeField('Date Modified', auto_now=True,
                                       blank=True, null=True)

    def __str__(self):
        return self.title
