from django.db import models

#importing a model from another app
from apps.fields.models import Field
#importing the third-party app CKEDITOR
from ckeditor.fields import RichTextField

#Employee main model
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
    skills = models.ManyToManyField('Skill')
    #adding this field that will be edited with the third-party app "CKEDITOR"
    #read the documentation for more information
    employee_cv = RichTextField()

    #changing the name of the model in the django admin interface and other customizations
    class Meta:
        verbose_name = "Employees list"
        verbose_name_plural = "Employees lists"
        #ordering table rows per id
        ordering = ['id']
        #disallowing the possibility to put a field that has the same attributes as before
        unique_together = ('first_name', 'last_name')

    def __str__(self):
        return "Employee id: {}, Employee name: {}, {}. Base: {}. Contact number: {}".format(self.id, self.first_name, self.last_name, self.base, self.contact_phone)
    


#secondary model Skills
class Skill(models.Model):
    skill = models.CharField("Skill", max_length=60)

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return "{}".format(self.skill)