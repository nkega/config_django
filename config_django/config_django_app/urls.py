from django.urls import path
from.import views

urlpatterns = [
    path("", views.index, name="index"),

    #path send_mail
    path("envoyer_email", views.envoyer_email, name="envoyer_email"),
]