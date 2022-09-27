from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.


def index(request):

    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        payment_form = ContactForm(request.POST)
        if payment_form.is_valid():
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            message = request.POST.get("message")
            name = request.POST.get("name")
            print(email)
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            send_mail(
                'Confirmation Message!',
                f"Hi {name}, I recieved your message regarding {subject}. Thanks for visiting my portfolio. "
                f"I will reply you as soon as possible.",
                email,
                [email],
                fail_silently=False,
                )
            send_mail(
                subject,
                message,
                email,
                ['chusmanjutt7812@gmail.com'],
                fail_silently=False,
            )
    return HttpResponseRedirect('/')
