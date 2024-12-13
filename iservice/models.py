from django.db import models
from uuid import uuid4


class User(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=12,unique=True)
    password = models.CharField(max_length=25)
    #creditcard = models.ForeignKey(CreditCard, on_delete=models.PROTECT, null=True, default='')

    def __str__(self):
        return f'E-mail: {self.email}'

class CreditCard(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    account = models.CharField(max_length=100)
    agency = models.CharField(max_length=50)
    validate = models.DateField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class Address(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid4)
    cep = models.CharField(max_length=100)
    complement = models.CharField(max_length=100)
    house_number = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    

class Service(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    custumer = models.ManyToManyField(User, related_name='services_customers')


class TypeService(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    name = models.CharField(max_length=60)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)

class Payment(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    date = models.DateTimeField()
    value = models.DecimalField(max_digits=7, decimal_places=2)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)