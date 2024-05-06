from django.db import models



class Category(models.Model):
    title = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.title


class Marka(models.Model):
    marka_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.marka_name

class Model(models.Model):
    model_name = models.CharField(max_length=32)
    marka_name = models.ForeignKey(Marka, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class Car(models.Model):
    car_name = models.CharField(max_length=32)
    price = models.PositiveIntegerField(default=0)
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    year = models.IntegerField(default=2024)
    type = models.BooleanField(default=True)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    volume = models.FloatField(default=0.8)

    def __str__(self):
        return self.car_name

