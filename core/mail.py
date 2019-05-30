from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_mail_template(subject, template_name, context, from_email, recipient_list=[settings.CONTACT_EMAIL], fail_silently=False):
    mensagem_html = render_to_string(template_name, context)
    mensagem_txt = striptags(mensagem_html)

    email = EmailMultiAlternatives(subject=subject, body=mensagem_txt, from_email=from_email, to=recipient_list)
    email.attach_alternative(mensagem_html, "text/html")
    email.send(fail_silently=fail_silently)