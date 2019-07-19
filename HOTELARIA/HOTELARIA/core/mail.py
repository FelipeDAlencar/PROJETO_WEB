from django.template.loader import render_to_string
from django.template.defaultfilters import striptags
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

def send_mail_template(assunto, template_name, contexto, recipient_list, from_email = settings.DEFAULT_FROM_EMAIL, fail_silently=False):
	mensagem_html = render_to_string(template_name, contexto)
	mensagem_de_texto = striptags(mensagem_html)
	email = EmailMultiAlternatives(subject=assunto, body=mensagem_de_texto, from_email=from_email,
			to=recipient_list
		)
	email.attach_alternative(mensagem_html, "text/html")
	email.send(fail_silently=fail_silently)