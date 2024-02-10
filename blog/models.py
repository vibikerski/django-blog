from django.db import models
from datetime import datetime, timedelta

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField()
    
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    
    def published_recently(self):
        return self.published_date + timedelta(days=7) > datetime.now()