from django.db import models

# Create your models here.

#creating the fields model
class Field(models.Model):
    #the first attribute represents the name of the model that will appear in admin
    name = models.CharField('Field Name', max_length=50)
    alt_name = models.CharField('Short Name', max_length=20)
    in_use = models.BooleanField("In use", default=True)

    #changing the name of the model in the django admin interface and other customizations
    class Meta:
        verbose_name = "Field option"
        verbose_name_plural = "Field options"
        #ordering table rows per id
        ordering = ['id']
        #disallowing the possibility to put a field that has the same attributes as before
        unique_together = ('name', 'alt_name')

    #modifying the magic method __str__
    def __str__(self):
        if self.in_use:
            return "Department name:{}, short name: {}, In use, ID: {}".format(self.name, self.alt_name, self.id)
        else:
            return "Department name:{}, short name: {}, Not in use, ID: {}".format(self.name, self.alt_name, self.id)

