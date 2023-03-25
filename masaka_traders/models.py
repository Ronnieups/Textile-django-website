from django.db import models

class User(models.Model):
    UserId = int(10)
    Type = (1=Old customer, 2=New customer)

