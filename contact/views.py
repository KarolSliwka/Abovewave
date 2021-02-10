from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from .forms import ContactForm
from offer.models import Offer


def contact(request):
    """A view to render Contact Page including Contact Form."""

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            from_email = contact_form.cleaned_data['from_email']
            subject = contact_form.cleaned_data['subject']
            offer = contact_form.cleaned_data['offer']
            message = contact_form.cleaned_data['message']

            if offer != None:
                found_offer = get_object_or_404(Offer, pk=request.POST.get('offer'))
                found_offer = found_offer.name
                my_subject = subject
            else:
                found_offer = "No offer selected"
                my_subject = subject

            html_msg = render_to_string(
                'includes/emails/email.html', {'name': name, 'subject': my_subject, 
                                        'message': message, 'from_email':from_email, 'offer':found_offer })
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                    html_message=html_msg, fail_silently=False)

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('/contact', messages.success(request, 
                            'Dear ' + name.title() + ', thanks for contacting us!  \
                                        We will answer in lightning speed.'))
        else: 
            return redirect('/contact', 
                            messages.info(request, 'Something went wrong..'))
                            
    else:
        contact_form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)



def contact_offer(request, offer_id):

    offer = get_object_or_404(Offer, pk=offer_id)

    if request.method == 'GET':
        if offer.id:
            try:
                contact_form = ContactForm(initial={
                    'subject': 'Offer Related',
                    'offer': offer.id,
                    }
                )
            except Offer.DoesNotExist:
                contact_form = ContactForm()
        else:
            contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            from_email = contact_form.cleaned_data['from_email']
            subject = contact_form.cleaned_data['subject']
            offer = contact_form.cleaned_data['offer']
            message = contact_form.cleaned_data['message']

            if offer != None:
                found_offer = offer.name
                my_subject = subject
            else:
                found_offer = "No offer selected"
                my_subject = subject

            html_msg = render_to_string(
                'includes/emails/email.html', {'name': name, 'subject': my_subject, 
                                        'message': message, 'from_email':from_email, 'offer': found_offer})
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                    html_message=html_msg, fail_silently=False)

            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            return redirect('/contact', messages.success(request, 
                            'Dear ' + name.title() + ', thanks for contacting us!  \
                                        We will answer in lightning speed.'))
        else: 
            return redirect('/contact', 
                            messages.info(request, 'Something went wrong..'))

    template = 'contact/contact.html'
    context =  {
        'contact_form': contact_form
        }

    return render(request, template, context)