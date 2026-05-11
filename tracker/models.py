from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Nutrients(models.Model):
    food = models.CharField(max_length=200)
    fat = models.FloatField()
    carbs = models.FloatField()
    calorie = models.IntegerField()
    protein = models.FloatField()

    def __str__(self):
        return self.food

    class Meta:
        verbose_name = "Nutrient"
        verbose_name_plural = "Nutrition Data"

class FoodConsumed(models.Model):
    food_consumed = models.ForeignKey(Nutrients, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Food Consumed"
        verbose_name_plural = "Foods Consumed"
    