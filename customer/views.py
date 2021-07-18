from django.shortcuts import render
from .models import customerDetail, transferDetail
from django.contrib import messages
# Create your views here.
def customer(request):
    customer = customerDetail.objects.all()
    context = {
        'customer' : customer
    }
    return render(request, 'customer.html', context)

def history(request):
    transfer = transferDetail.objects.all()
    context = {
        'transfer' : transfer
    }
    return render(request, 'history.html', context)

def profile(request, cust_id):
    sender = customerDetail.objects.get(id=cust_id)
    recieverAll = customerDetail.objects.all

    if request.method == 'POST':
        reciever_id = request.POST['reciever']

        if request.POST['amount_transfer'] == '' or float(request.POST['amount_transfer']) <= 0:
            messages.warning(request, 'Please Enter a Valid Amount!')
        else:
            amount_transfer = float(request.POST['amount_transfer'])

        if reciever_id == 'Select One':
            messages.warning(request, 'Please Select a Reciever')
        else:
            reciever = customerDetail.objects.get(id=reciever_id)
            if not amount_transfer > sender.balance:
                sender.balance = sender.balance - amount_transfer
                reciever.balance = reciever.balance + amount_transfer
                sender.save()
                reciever.save()
                transferDetail(sender=sender, reciever=reciever, amount=amount_transfer).save()
                messages.success(request, 'Transfer Successful!')
            else:
                messages.warning(request, 'Insufficient Balane')

    context = {
        'sender' : sender,
        'recieverAll' : recieverAll
    }
    return render(request, 'profile.html', context)