from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'portfolio/home.html')

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})

from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                f'Contact Form Submission from {name}',  # subject
                message,  # message
                email,  # from email
                ['vinaychalla654@gmail.com'],  # to your email
            )

            return render(request, 'portfolio/contact_success.html')

    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})
