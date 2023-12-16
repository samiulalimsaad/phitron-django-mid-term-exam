from django.contrib.auth.models import User
from django.db import models

from brand.models import Brand


class Car(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="car/car_images/", null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)  # Add the quantity field

    def __str__(self):
        return f"{self.name} - {self.brand}"


class Buy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.car.quantity -= 1
        self.car.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} bought {self.car.name} on {self.purchase_date}"
