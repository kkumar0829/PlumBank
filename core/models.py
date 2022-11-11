from django.db import models


# Create your models here.
class BankUser(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()


class Account(models.Model):
    bankuser = models.ForeignKey(BankUser, on_delete=models.CASCADE)
    account_number = models.IntegerField(default=4000)
    balance = models.IntegerField(default=1000)


class Transaction(models.Model):
    account_number = models.IntegerField()
    transaction_type = models.CharField(max_length=6)
    peer_account_number = models.IntegerField()
    amount = models.IntegerField()
