from django.db import models

# Create your models here.
class UserComment(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    comment = models.CharField(max_length=1000)

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookingdate = models.DateField()
    def get_item(self):
        return f'{self.name} for {str(self.no_of_guests)}'


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
