from django.db import models

class Project (models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return f"{self.title} - {self.description}"


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"