from django.db import models

# Create your models here.

#creating the fields model
class Field(models.Model):
    #the first attribute represents the name of the model that will appear in admin
    name = models.CharField('Field Name', max_length=50)
    alt_name = models.CharField('Short Name', max_length=20)
    in_use = models.BooleanField("In use", default=True)

    #modifying the magic method __str__
    def __str__(self):
        return "Department name:{}, department short name: {}, is the department in use? {}. ID of the field: {}".format(self.name, self.alt_name, self.in_use, self.id)

