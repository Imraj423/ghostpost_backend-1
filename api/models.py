from django.db import models
from django.utils import timezone

# Create your models here.
class GhostPost(models.Model):
    boast = models.BooleanField(default=False)
    roast = models.BooleanField(default=False)
    post_input = models.CharField(max_length=150)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    sum_of_votes = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_input
