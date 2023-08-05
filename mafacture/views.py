from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib import messages

# Create your views here.

class HomeView(View):
    """Main view"""

    templates_name = 'index.html'
    factures = Facture.objects.select_related('client', 'save_by').all()

    context = {
        'factures': factures
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name, self.context)

    def post(request, self, *args, **kwargs):
        return render(request, self.templates_name, self.context)

class AjouterClientView(View):
    """ajouter nouveau client"""

    templates_name = 'ajouter_client.html'

    def get(self, request, *args, **kwargs):
         return render(request, self.templates_name)

    def post(self, request, *args, **kwaegs):
        
        data = {
            'nom': request.POST.get('nom'),
            'email': request.POST.get('email'),
            'telephone': request.POST.get('telephone'),
            'adresse': request.POST.get('adresse'),
            'sexe': request.POST.get('sexe'),
            'age': request.POST.get('age'),
            'ville': request.POST.get('ville'),
            'code_postal': request.POST.get('code'),
            'save_by': request.user

        }
        try:
            created = Client.objects.create(**data)
            if created:
                messages.success(request, "Client enregistré avec succès.")
            else:
                messages.error(request, "Désolé, Données corrompues, reessayer.")

        except Exception as e:
            messages.error(request, f"Désolé, le système a détecté l'anomalie suivante {e}.")
            return render(request, self.templates_name)