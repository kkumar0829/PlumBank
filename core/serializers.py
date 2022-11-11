from rest_framework import serializers
from core.models import BankUser, Transaction, Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankUser
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    peer_age = serializers.SerializerMethodField()
    peer_name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return Account.objects.get(account_number=obj.account_number).bankuser.name

    def get_age(self, obj):
        return Account.objects.get(account_number=obj.account_number).bankuser.age

    def get_peer_name(self, obj):
        return Account.objects.get(account_number=obj.peer_account_number).bankuser.name

    def get_peer_age(self, obj):
        return Account.objects.get(account_number=obj.peer_account_number).bankuser.age

    class Meta:
        model = Transaction
        fields = (
            'id',
            'account_number',
            'name',
            'age',
            'transaction_type',
            'peer_account_number',
            'peer_name',
            'peer_age',
            'amount'
        )
