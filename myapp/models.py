from django.db import models

class ListData(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True, auto_now_add=False, auto_now=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title