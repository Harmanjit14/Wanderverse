from django.db import models

class Leaderboard(models.Model):
    user = models.CharField(max_length=256)
    score = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score', 'date']

    def __str__(self):
        return f"{self.user} - {self.score}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if Leaderboard.objects.count() > 5:
            lowest_score_entry = Leaderboard.objects.order_by('score', 'date').first()
            lowest_score_entry.delete()