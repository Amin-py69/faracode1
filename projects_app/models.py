from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    address = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to='projects_img')

    def __str__(self):
        return self.title