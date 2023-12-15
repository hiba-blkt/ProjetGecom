from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CaissierManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'email est requis')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('admin', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Caissier(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nom = models.CharField(max_length=255)
    username = models.CharField(max_length=255,unique=True)
    prenom = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    username="admin"
    objects = CaissierManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nom', 'prenom', 'poste']

    def _str_(self):
        return self.email
class Client(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)

class DetailBL(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    bl = models.ForeignKey('BonLivraison', on_delete=models.CASCADE)
    qte = models.DecimalField(max_digits=8, decimal_places=2)

class Article(models.Model):
    designation = models.CharField(max_length=255)
    prix_ht = models.DecimalField(max_digits=8, decimal_places=2)
    tva = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.DecimalField(max_digits=8, decimal_places=2)
    famille = models.ForeignKey('Famille', on_delete=models.CASCADE)

class Famille(models.Model):
    famille = models.CharField(max_length=255)

class BonLivraison(models.Model):
    date = models.DateField()
    client = models.ForeignKey('Client', null=True, on_delete=models.CASCADE)
    caissier = models.ForeignKey('Caissier', on_delete=models.CASCADE)