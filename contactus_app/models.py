from django.db import models


# Create your models here.


class ContactUs(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    whatsapp = models.CharField(max_length=100, default='te.me2222')
    telegram = models.CharField(max_length=100, default='wa.me2222')
    instagram = models.CharField(max_length=100, default='in.me2222')


class Message(models.Model):
    fname = models.CharField(max_length=50)
    email = models.EmailField()
    sub = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self):
        return f'{self.fname}, {self.email}'
