from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return "User %s %s" % (self.name, self.email)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"



