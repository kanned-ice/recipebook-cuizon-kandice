from django.urls import path
from .views import (
    RecipeListView, RecipeDetailView,
    RecipeCreateView, RecipeImageUploadView
    )


app_name = "ledger"

urlpatterns = [
   path('recipes/list/', RecipeListView.as_view(), name="recipes_list"),
   path('recipe/<int:pk>/', RecipeDetailView.as_view(), name="recipe_detail"),
   path('recipe/add/', RecipeCreateView.as_view(), name="recipe_form"),
   path('recipe/<int:pk>/add_image/', RecipeImageUploadView.as_view(),
        name="image_form")
]
