from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.CharField(
        max_length=50
    )
    anons=models.CharField(
        max_length=200
    )
    full_text=models.TextField(
        max_length=1000
    )
    date=models.DateTimeField(
        
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='new'
        verbose_name_plural='news'
    