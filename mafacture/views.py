from django.shortcuts import render
from django.views import View
from .models import *
from django.contrib import messages
from django.db import transaction

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

class AjouterFactureView(View):
    """ajouter nouvelle facture view"""

    templates_name = 'ajouter_facture.html'
    clients = Client.objects.select_related('save_by').all()

    context = {
        'clients': clients 
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.templates_name, self.context)

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        print(request.POST)
        items = []

        try:
            client = request.POST.get('client')
            type = request.POST.get('type_facture')
            articles = request.POST.getlist('articles')
            qtes = request.POST.get('qte')
            unitaires =  request.POST.get('unitaire')
            total_a = request.POST.getlist('total-a')
            total = request.POST.get('total')
            commentaire = request.POST.get('commentaire')

            facture_object = {
                'client_id': client,
                'save_by': request.user,
                'total': total,
                'type_facture': type, 
                'commentaires': commentaire

            }
                
            facture = Facture.objects.create(** facture_object)
            for index, article in enumerate(articles):
                data = Articles(
                    facture_id = facture.id,
                    name = article,
                    quantite = qtes[index],
                    prix_unitaire = unitaires[index],
                    total = total_a[index],

                )
                
                items.append[data]
            created = Article.objects.bulk_create(items)
            if created:
                messages.success(request, "Data saved successfully.")
            
            else:
                messages.error(request, "Désolé, réessayer d'envoyer car les données sont corrompues.")
        
        except Exception as e:
            messages.error(request, f"Désolé, l'erreur suivante est arrivée {e}.")

        return render(request, self.templates_name, self.context)