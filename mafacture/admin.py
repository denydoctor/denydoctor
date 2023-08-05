from django.contrib import admin
from .models import *

# Register your models here.
class AdminClient(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'adresse', 'sexe', 'age', 'ville', 'code_postal')

class AdminFacture(admin.ModelAdmin):
     list_display = ('client', 'save_by', 'facture_date_time', 'total', 'last_updated_date', 'paye', 'type_facture')

class AdminArticle(admin.ModelAdmin):
    list_display = ('facture', 'nom', 'quantite', 'prix_unitaire', 'total')

admin.site.register(Client, AdminClient)
admin.site.register(Facture, AdminFacture)
admin.site.register(Article, AdminArticle)
