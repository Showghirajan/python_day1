from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

def bank(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Get the latest account number
            latest_account = Customer.objects.order_by('-accno').first()
            # Set the initial account number to 8000 if no accounts exist
            next_accno = 8000 if not latest_account else latest_account.accno + 1
            # Save the form data with the generated account number
            form.instance.accno = next_accno
            form.save()
            return redirect('created', accno=next_accno)
    else:
        form = CustomerForm()
    return render(request, 'app3/index1.html', {'form': form})

def created(request, accno):
    return render(request, 'app3/index2.html', {'accno': accno})
