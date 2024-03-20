from django.db import models

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length = 50)
    color = models.CharField(max_length=7, default='#FFD700')
    def __str__(self):
        return self.post_title

class Task(models.Model):
    STATUS_CHOICES = {
        'NS': 'Not Started',
        'DO': 'Doing',
        'DN': 'Done',
        'CA': 'Canceled'
    }
    
    DIFF_LEVEL_CHOICES = {
        'VE': 'Very Easy',
        'E' : 'Easy',
        'M' : 'Medium',
        'H' : 'Hard',
        'VH' : 'Very Hard'
    }
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length = 150)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=STATUS_CHOICES['NS'])
    difficult_level = models.CharField(max_length = 2, choices=DIFF_LEVEL_CHOICES)
    deadline = models.DateTimeField("deadline")
    
    def __str__(self):
        return self.text
    