from django.contrib import admin

from core.models import *

admin.site.register(BankUser)
admin.site.register(Account)
admin.site.register(Transaction)
