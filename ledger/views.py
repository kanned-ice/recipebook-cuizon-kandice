from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Recipe

class RecipeListView(ListView):
   model = Recipe
   template_name = "ledger/recipes.html"

class RecipeDetailView(DetailView):
   model = Recipe
   template_name = "ledger/recipe_list.html"