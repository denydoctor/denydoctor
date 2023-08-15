from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    """
    Nom: Client model definition
    """
    SEXE_TYPES = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    nom = models.CharField(max_length=130)
    email = models.EmailField()
    telephone = models.CharField(max_length=120)
    adresse = models.CharField(max_length=80)
    sexe = models.CharField(max_length=1, choices=SEXE_TYPES)
    age = models.CharField(max_length=15)
    ville = models.CharField(max_length=30)
    code_postal = models.CharField(max_length=15)
    date_creation = models.DateTimeField(auto_now_add=True)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.nom   

class Facture(models.Model):
    """
    nom: Facture model definition
    Description:
    auteur: denybothamatuba@gmail.com
    """
    TYPE_FACTURE = (
        ('R', 'RECU'),
        ('P', 'PROFORMA FACTURE'),
        ('F', 'FACTURE')
    )
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    save_by = models.ForeignKey(User, on_delete=models.PROTECT)
    facture_date_time = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10000, decimal_places=2)
    last_updated_date = models.DateTimeField(null=True, blank=True)
    paye = models.BooleanField(default=False)
    type_facture = models.CharField(max_length=1, choices=TYPE_FACTURE)
    commentaires = models.TextField(null=True, max_length=1000, blank=True)

    class Meta:
        verbose_name = "Facture"
        verbose_name_plural = "Factures"

    def __str__(self):
        return f"{self.client.nom}_{self.facture_date_time}"

    @property
    def get_total(self):
        articles = self.article_set.all()
        total = sum(article.get_total for article in articles)
        return total

class Article(models.Model):
    """
    nom: Article model definition
    Description:
    auteur: denybothamatuba@gmail.com
    """

    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    nom =  models.CharField(max_length=30)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=1000, decimal_places=2)
    total = models.DecimalField(max_digits=1000, decimal_places=2)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    @property
    def get_total(self):
        total = self.quantite * self.prix_unitaire
        return total

