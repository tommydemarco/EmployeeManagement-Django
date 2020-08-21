from django.db import models

#importing a model from another app
from apps.fields.models import Field

# Create your models here.

class Employee(models.Model):
    #creating the base choices 
    BASE_CHOICES = (
        ("AGP", "Malaga"),
        ("EDI", "Edinburgh"),
        ("TFS", "Tenerife South"),
        ("PVD", "Providence"),
        ("DUB", "Dublin"),
    )
    #the first attribute represents the name of the model that will appear in admin
    first_name = models.CharField('First name', max_length=50)
    last_name = models.CharField('Last Name', max_length=20)
    contact_phone = models.IntegerField('Contact Number')
    address = models.CharField('Adress', max_length=80)
    base = models.CharField('Base', max_length=3, choices=BASE_CHOICES)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    #image = models.ImageField()

    def __str__(self):
        return "Employee id: {}, Employee name: {}, {}. Base: {}. Contact number: {}".format(self.id, self.first_name, self.last_name, self.base, self.contact_phone)
    