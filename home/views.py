from django.shortcuts import render, HttpResponse
from home.models import Contact, Review
from datetime import datetime
from django.contrib import messages
#import smtplib

#def send_email(to, content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.starttls()
    #server.login('kalemangofarms@gmail.com', 'kalemango12#')
    #server.ehlo()
    #server.sendmail('kalemangofarms@gmail.com', to, content)
    #server.close()

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
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
    
        messages.success(request, 'Your message has been sent!')
        
    return render(request, 'contact.html')
    
def review(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        rev = Review(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        rev.save()
        messages.success(request, 'Your review has been sent!')
    return render(request, 'review.html')



# Create your views here.
