from django import forms

from .models import Recipe, RecipeImage


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'author']

class ImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = '__all__'