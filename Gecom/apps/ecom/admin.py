from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Caissier

class CaissierAdmin(UserAdmin):
    list_display = ('email', 'nom', 'prenom', 'poste', 'admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informations personnelles', {'fields': ('nom', 'prenom', 'poste')}),
        ('Permissions', {'fields': ('admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'nom', 'prenom', 'poste', 'admin'),
        }),
    )
    search_fields = ('email', 'nom', 'prenom')
    ordering = ('email',)

# Enregistrement du modèle Caissier avec sa configuration admin personnalisée
admin.site.register(Caissier, CaissierAdmin)

from .models import Client, DetailBL, Article, Famille, BonLivraison

# Configurations pour le modèle Client
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'adresse', 'ville')
    search_fields = ('nom', 'prenom')

admin.site.register(Client, ClientAdmin)

# Configurations pour le modèle DetailBL
class DetailBLAdmin(admin.ModelAdmin):
    list_display = ('article', 'bl', 'qte')
    list_filter = ('article', 'bl')
    search_fields = ('article_designation', 'bl_date')

admin.site.register(DetailBL, DetailBLAdmin)

# Configurations pour le modèle Article
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('designation', 'prix_ht', 'tva', 'stock', 'famille')
    list_filter = ('famille',)
    search_fields = ('designation',)

admin.site.register(Article, ArticleAdmin)

# Configurations pour le modèle Famille
class FamilleAdmin(admin.ModelAdmin):
    list_display = ('famille',)
    search_fields = ('famille',)

admin.site.register(Famille, FamilleAdmin)

# Configurations pour le modèle BonLivraison
class BonLivraisonAdmin(admin.ModelAdmin):
    list_display = ('date', 'client', 'caissier')
    list_filter = ('client', 'caissier')
    search_fields = ('client_nom', 'caissier_nom')

admin.site.register(BonLivraison, BonLivraisonAdmin)