from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200, default='none')
    nutriscore = models.IntegerField(default=0)
    picture_url = models.CharField(max_length=200, default='none')
    off_url = models.CharField(max_length=200, default='none')
    sugar_100g = models.IntegerField(default=0)
    salt_100g = models.IntegerField(default=0)
    carbohydrates_100g = models.IntegerField(default=0)
    sodium_100g = models.IntegerField(default=0)
    saturated_fat_100g = models.IntegerField(default=0)
    proteins_100g = models.IntegerField(default=0)
    fat_100g = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Food_category(models.Model):
    food_id = models.ForeignKey('Food', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=200, default='none')

    def __str__(self):
        return self.name