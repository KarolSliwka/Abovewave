from django.db import models

class Info(models.Model):
    """Information single block model."""
    image = models.ImageField(upload_to="images/info", null=True, blank=True)
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name


class InfoLineItem(models.Model):
    """This class will create a single lineitem for Info Model."""

    info = models.ForeignKey(Info,null=False, blank=False,on_delete=models.CASCADE, related_name='lineitems')
    description = models.TextField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return f'Name {self.description} on Order {self.info}'