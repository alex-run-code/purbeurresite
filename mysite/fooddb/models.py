from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200, default='none', unique=True)
    nutriscore = models.CharField(max_length=200, default='none')
    picture_url = models.CharField(max_length=200, default='none')
    off_url = models.CharField(max_length=200, default='none')
    sugar_100g = models.FloatField(default=0)
    salt_100g = models.FloatField(default=0)
    carbohydrates_100g = models.FloatField(default=0)
    sodium_100g = models.FloatField(default=0)
    saturated_fat_100g = models.FloatField(default=0)
    proteins_100g = models.FloatField(default=0)
    fat_100g = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Food_category(models.Model):
    food = models.ForeignKey('Food', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=200, default='none', unique=True)

    def __str__(self):
        return self.name