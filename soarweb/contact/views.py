from __future__ import unicode_literals
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template

from .forms import ContactForm
# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        redirect_to = '/'

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            to_mail = [instance.email]
            subject = "Web Mail Soar"
            from_email = settings.DEFAULT_FROM_EMAIL
            context = {
                'first_name': instance.first_name,
                'last_name': instance.last_name,
                'phone': instance.phone,
                'email': instance.email,
                'message': instance.message,
                'created': instance.created,
            }
            with open(settings.BASE_DIR + "/templates/contactoapp/contacto_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("contactoapp/contacto_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            subject = "Copia: WEB MAIL SOAR"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_mail = ['paul@soar.cl']
            with open(settings.BASE_DIR + "/templates/contactoapp/contacto_template_detail.txt") as f:
                signup_message = f.read()
            html_template = get_template("contactoapp/contacto_template_detail.html").render(context)
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_mail)
            message.attach_alternative(html_template, "text/html")
            message.send()

            return redirect(redirect_to)
    else:
        form = ContactForm()
    return form
