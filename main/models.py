from django.db import models
import uuid #For unique characters
# Create your models here.
class Topic(models.Model):
    topic_id =  models.UUIDField(default=uuid.uuid4, editable=False,unique=True, null=True)
    name =  models.CharField(max_length=200)
    date_created =models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self) -> str:
        return f'{self.name}'

class Responses(models.Model):
    res_id =  models.UUIDField(default=uuid.uuid4, editable=False,unique=True, null=True)
    topic =      models.ForeignKey(Topic,on_delete=models.CASCADE,null=True)
    comment =  models.CharField(max_length=20000)
    date_created =models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)
    def __str__(self) -> str:
        return f'{self.topic.name } --- response {self.id}'