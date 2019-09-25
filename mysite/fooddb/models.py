from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=200)
    nutriscore = models.IntegerField()

    def __str__(self):
        return self.name

class Food_category(models.Model):
    food_id = models.ForeignKey('Food', on_delete=models.CASCADE)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name