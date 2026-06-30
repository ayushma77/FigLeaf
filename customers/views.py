from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Customer
from .forms import CustomerForm


@login_required
def customer_list(request):
    search = request.GET.get("search", "")

    customers = Customer.objects.all().order_by("-created_at")

    if search:
        customers = customers.filter(name__icontains=search)

    return render(request, "customers/customer_list.html", {
        "customers": customers,
        "search": search,
    })


@login_required
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully.")
            return redirect("customer_list")
    else:
        form = CustomerForm()

    return render(request, "customers/customer_form.html", {
        "form": form,
        "title": "Add Customer",
        "button_text": "Save Customer",
    })


@login_required
def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)

    return render(request, "customers/customer_detail.html", {
        "customer": customer,
    })