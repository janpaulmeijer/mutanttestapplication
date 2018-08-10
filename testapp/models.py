from django.db import models


class Account(models.Model):
    account_number = models.CharField(max_length = 100)
    account_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.account_name