from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        )
    name = models.CharField(max_length=50)
    short_bio = models.TextField(validators=[MinLengthValidator(
        255, 'the field must contain at least 255 characters')])

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe_list', args=[str(self.id)])


class Recipe(models.Model):
    name = models.CharField(max_length=50)

    author = models.ForeignKey(
       Profile,
       on_delete=models.CASCADE,
       related_name='recipe'
       )

    created_on = models.DateTimeField(auto_now_add=True)

    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', kwargs={'pk': self.pk})


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)

    ingredient_key = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )

    recipe_key = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )

    def __str__(self):
        return f"{self.ingredient_key.name}: {self.quantity}"
