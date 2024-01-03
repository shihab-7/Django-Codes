from django.contrib import admin
from .models import Transaction
from .views import send_transaction_email
# Register your models here.
@admin.register(Transaction)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ['account', 'amount','balance_after_transaction','transaction_type', 'loan_approved']

    def save_model(self, request, obj, form, change):
        if obj.loan_approved == True:
            obj.account.balance += obj.amount
            obj.balance_after_transaction = obj.account.balance
            send_transaction_email(obj.account.user, obj.amount, "Loan Approval", "transactions/admin_email.html")
            obj.account.save()
            super().save_model(request, obj, form, change)

    # loan approve howar por database a balance auto update hoye jabe sathe frontend a user er account a o update hoye jabe.