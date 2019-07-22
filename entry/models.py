from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Entry(models.Model):
    author = models.ForeignKey('auth.User',on_delete= models.CASCADE)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete= models.CASCADE)
    title = models.CharField(max_length = 300)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    last_saved_date = models.DateTimeField(blank = True, null = True)

    def last_save(self):
        self.last_saved_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title 