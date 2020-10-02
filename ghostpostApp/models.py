from django.db import models
from django.utils import timezone

class ghostpost(models.Model):
    
    BOAST = 'B'
    ROAST = 'R'
    
    ghostpost_choice = models.CharField(max_length=1, blank=True,
        choices=[(BOAST, 'Boast'), (ROAST, 'Roast')])
    ghostpost_content = models.CharField(blank=True, 
        max_length=280, verbose_name='Content')
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.ghostpost_content

    @property
    def vote_score(self):
        return self.upvotes - self.downvotes