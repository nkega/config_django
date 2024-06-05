from django.shortcuts import render
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, "index.html")

#pour l'envoi des mails
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

#  methode d'envoi d'un email en django
def envoyer_email(request):
    sujet = 'vous avez recu un mail d\'un developpeur pro'
    message = 'Bonjour ici Brice_Dev, developpeur BackEnd professionnel'
    adresse_email = 'bnkega@gmail.com'
    envoyeur = settings.EMAIL_HOST_USER 

    try:
        send_mail(sujet, message, envoyeur, [adresse_email])
        return HttpResponse('Email envoyé avec succès')
    except:
        return HttpResponse('Erreur lors de l\'envoi de l\'email')