from django.db import models

#importing the employee model
'''from apps.employees.models import Employee'''

# Create your models here.

#creating the fields model
class Field(models.Model):
    #the first attribute represents the name of the model that will appear in admin
    field_name = models.CharField('Field Name', max_length=50)
    alt_name = models.CharField('Short Name', max_length=20)
    in_use = models.BooleanField("In use", default=True)

    '''field_manager = models.ForeignKey(Employee, on_delete=models.CASCADE)'''

    #changing the name of the model in the django admin interface and other customizations
    class Meta:
        verbose_name = "Field option"
        verbose_name_plural = "Field options"
        #ordering table rows per id
        ordering = ['id']
        #disallowing the possibility to put a field that has the same attributes as before
        unique_together = ('field_name', 'alt_name')

    #modifying the magic method __str__
    def __str__(self):
        if self.in_use:
            return "{}, short name: {}, In use, ID: {}".format(self.field_name.upper(), self.alt_name, self.id)
        else:
            return "{}, short name: {}, Not in use, ID: {}".format(self.field_name.upper(), self.alt_name, self.id)

