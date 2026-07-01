from django.shortcuts import render
from home.models import Contact, Review
from datetime import date
from django.contrib import messages


def index(request):
    return render(request, 'index.htm')


def mango_prices(request):
    return render(request, 'mangoprice.htm')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=date.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')


def review(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        rev = Review(name=name, email=email, phone=phone, desc=desc, date=date.today())
        rev.save()
        messages.success(request, 'Your review has been sent!')
    return render(request, 'review.html')
