from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .models import Transaction
from .forms import DepositeForm, WithdrawForm, LoanRequestForm
from .constants import DEPOSITE, WITHDRAWAL,LOAN, LOAN_PAID
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
from django.db.models import Sum
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string  #html template k string a convert kore



# bar bar mail pathanor system na likhe just akta function banay rakhbo oita jayga moto call korlei bar bar lekhar dorkar porbe na
def send_transaction_email(user, amount, subject, template):
    message = render_to_string(template, {
        'user' : user,
        'amount' : amount,
    })

    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()

# Create your views here.
# eita akta base view banay nisi jeta prottek class er vitor inherrit kore code er length komay ana jabe
class TransactionCreateMixin(LoginRequiredMixin, CreateView):

    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')


# jokhon e akta new form create hobe tokhon forms.py a amra j constructor diye fields edit er kaj kortesilam __init__ er moddhe oi function a j kwargs er data ta lagto oita amra eikha theke pass kore dissi oita
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account' : self.request.user.account,
        })

        return kwargs
    
    # akoi template use kore ak ak somoy ak ak title diye ak ak kaj korar jonno frontend a title ta bar bar update korar kaj ei function korbe
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title' : self.title,
        })
        return context



class DepositeMoneyView(TransactionCreateMixin):
    form_class = DepositeForm
    title = 'Deposite Money'

# ei initial data amrai backend theke pass kore dissi frontend a jeta user just dekhte parbe but chose ba edit korte pabe na
    def get_initial(self):
        initial = {'transaction_type': DEPOSITE}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        # user jokhon e valid balance diye form submit dibe tokhon e balance field er value update hoye jabe
        account.save(
            update_fields = ['balance']
        )

        messages.success(self.request, f'{amount} $ is deposited successfully in your account')
        
        # # user successfully deposit korle mail chole jabe
        # mail_subject = 'Deposit Message'
        # message = render_to_string('transactions/deposite_email.html', {
        #     'user': self.request.user,
        #     'amount': amount,
        # })
        # to_email = self.request.user.email
        # send_email = EmailMultiAlternatives( mail_subject,'',to=[to_email])
        # send_email.attach_alternative(message, 'text/html')
        # send_email.send()
        # bar bar na likhe direct function banay niye call kora hoidse

        send_transaction_email(self.request.user, amount, "Deposite Message", "transactions/deposite_email.html")
        
        
        return super().form_valid(form)
    

class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'

# ei initial data amrai backend theke pass kore dissi frontend a jeta user just dekhte parbe but chose ba edit korte pabe na
    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance -= amount
        # user jokhon e valid balance diye form submit dibe tokhon e balance field er value update hoye jabe
        account.save(
            update_fields = ['balance']
        )

        messages.success(self.request, f'{amount} $ is withdrew successfully from your account')

        send_transaction_email(self.request.user, amount, "Withdrawal Message", "transactions/withdrawal_email.html")
        
        return super().form_valid(form)
    

class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request For Loan'

# ei initial data amrai backend theke pass kore dissi frontend a jeta user just dekhte parbe but chose ba edit korte pabe na
    def get_initial(self):
        initial = {'transaction_type': LOAN}
        return initial
    
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(account = self.request.user.account, transaction_type = LOAN, loan_approved = True).count()

        if current_loan_count >= 3:
            return HttpResponse("You have Crossed Your Limits")
        messages.success(self.request, f'Loan Request for {amount} $ is sent to admin successfully')
        send_transaction_email(self.request.user, amount, "Loan Request Message", "transactions/loan_email.html")
        
        return super().form_valid(form)
    

class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    balance = 0
    context_object_name = 'report_list'

    def get_queryset(self):

        # jodi user kono type transaction filter na kore sob dekhte chay tobe sob dekhabe
        queryset= super().get_queryset().filter(
            account = self.request.user.account
        )

        # frontend theke start date r end date ashbe 
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

      # specific user er jonno date wise history filter kora hosse
        if start_date_str and end_date_str:

            # date string format a asa oita akhon date format a convert kora hoise
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

            # timestamp boro theke soto porjonto niye filter kora hoise gte te greater than r lte less than
            queryset = queryset.filter(timestamp__date__gte = start_date , timestamp__date__lte = end_date)

            # filter korle balance
            self.balance = Transaction.objects.filter(timestamp__date__gte = start_date, timestamp__date__lte = end_date).aggregate(Sum('amount'))['amount__sum']
            # to know more about aggrigate function google it

        else :
            # filter na korle balance
            self.balance = self.request.user.account.balance

        # return queryset.distinct() #distinct() function dublicate value gulo baad diye dey
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account' : self.request.user.account
        })
        return context
    

class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Transaction, id= loan_id)

# user er loan approved hoile loan pay korbe
        if loan.loan_approved:
            user_account = loan.account
            if loan.amount < user_account.balance: #user er main balance loan er theke beshi hoilei loan pay korte parbe
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.transaction_type = LOAN_PAID
                loan.save()
                return redirect('loan_list')
            
            else:
                messages.error(self.request, f'Loan amount is greater than available balance')
        return redirect('loan_list')
            

class LoanListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/loan_request.html'
    context_object_name = 'loans' # ei nam ta set kore dilam jate vejal sarai ei nam diye access korte pari data gulo

    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(account=user_account, transaction_type = LOAN)
        return queryset