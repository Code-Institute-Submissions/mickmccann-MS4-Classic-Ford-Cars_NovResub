from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255, default="",
                            null=False, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=255, default="",
                               null=False, blank=False)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
