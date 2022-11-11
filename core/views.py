from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core import constants
from core.serializers import UserSerializer, TransactionSerializer, AccountSerializer
from core.models import *
from django.core.paginator import Paginator


class CreateUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        account_number = constants.BUFFER_VALUE + serializer.data.get('id')
        acc_serializer = AccountSerializer(
            data={
                'account_number': int(account_number),
                'bankuser': serializer.data.get('id'),



            })
        acc_serializer.is_valid(raise_exception=True)
        acc_serializer.save()
        instance.save()
        return Response({"Thanks for registering in our bank. You account number is : ": account_number})


class AllTransactions(APIView):
    def post(self, request):
        if request.data["account_number"] == request.data["peer_account_number"]:
            return Response("Account number and Peer Account Number can't be same",status=status.HTTP_404_NOT_FOUND)
        else:
            pass
        if request.data["transaction_type"] == 'credit':
            peer_bal = Account.objects.get(account_number=request.data["peer_account_number"]).balance
            if peer_bal < int(request.data["amount"]):
                return Response("Not Enough Balance")
            else:
                pass
        elif request.data["transaction_type"] == 'debit':
            bal = Account.objects.get(account_number=request.data["account_number"]).balance
            if bal < int(request.data["amount"]):
                return Response("Not Enough Balance")
            else:
                pass
        else:
            return Response("Kindly Choose from credit/debit only")
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        account_number = instance.account_number
        peer_account_number = instance.peer_account_number
        amount = instance.amount
        transaction_type = instance.transaction_type
        if transaction_type == 'credit':

            Transaction.objects.create(
                account_number=peer_account_number,
                transaction_type="debit",
                peer_account_number=account_number,
                amount=amount)
            bal = Account.objects.get(account_number=account_number).balance
            bal = bal + amount
            instance = Account.objects.get(account_number=account_number)
            instance.balance = bal
            instance.save()

            peer_bal = Account.objects.get(account_number=peer_account_number).balance
            peer_bal = peer_bal - amount
            peer_instance = Account.objects.get(account_number=peer_account_number)
            peer_instance.balance = peer_bal
            peer_instance.save()

        else:
            Transaction.objects.create(
                account_number=peer_account_number,
                transaction_type="credit",
                peer_account_number=account_number,
                amount=amount)
            bal = Account.objects.get(account_number=account_number).balance
            bal = bal - amount
            instance = Account.objects.get(account_number=account_number)
            instance.balance = bal
            instance.save()

            peer_bal = Account.objects.get(account_number=peer_account_number).balance
            peer_bal = peer_bal + amount
            peer_instance = Account.objects.get(account_number=peer_account_number)
            peer_instance.balance = peer_bal
            peer_instance.save()

        instance.save()
        return Response(f"{amount} has been successfully {transaction_type}ed")


class CheckBalance(APIView):
    def get(self, request, account_number):
        curr_balance = Account.objects.filter(account_number=account_number)
        if curr_balance:
            return Response(f"Your current remaining balance is : {curr_balance.first().balance}")
        else:
            return Response("Your account number doesn't exist. Please register!", status=status.HTTP_404_NOT_FOUND)


class CheckPassbook(APIView):
    def get(self, request, account_number):
        page_number = request.GET.get("page", 1)
        per_page = request.GET.get("per_page", 2)
        transactions = Transaction.objects.filter(account_number=account_number)
        paginator = Paginator(transactions, per_page)
        page_obj = paginator.get_page(page_number)
        paginated_list = page_obj.object_list
        serializer = TransactionSerializer(paginated_list, many=True)
        payload = {
            "page": {
                "current": page_obj.number,
                "has_next": page_obj.has_next(),
                "has_previous": page_obj.has_previous(),
            },
            "data": serializer.data
        }
        if transactions:
            return Response(payload, status=status.HTTP_200_OK)
        else:
            return Response("Your account number doesn't exist. Please register!", status=status.HTTP_404_NOT_FOUND)
