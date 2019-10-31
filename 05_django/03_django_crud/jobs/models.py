from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.TextField()
    past_job = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}번]: {self.name}|{self.past_job}'