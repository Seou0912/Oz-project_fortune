from django.db import models


class DailyQuote(models.Model):
    # nickname = models.CharField(max_length= 10)
    date = models.DateField(unique=True)
    quote = models.TextField()

    def __str__(self):
        return f"{self.date}: {self.quote}"
