from django.contrib import admin
from core.models import *
# Register your models here.
admin.site.register(BankUser)
admin.site.register(Account)
admin.site.register(Transaction)
