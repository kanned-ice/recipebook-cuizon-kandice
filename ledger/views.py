from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, RecipeImage


class RecipeListView(ListView):
    model = Recipe
    template_name = "ledger/recipe_list.html"


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "ledger/recipe_detail.html"
    redirect_field_name = None


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ['name', 'author']


class RecipeImageUploadView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    fields = ['image', 'description']
    template_name = "ledger/image_form.html"

    def form_valid(self, form):
        recipe_pk = self.kwargs['pk']
        form.instance.recipe = Recipe.objects.get(pk=recipe_pk)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe_pk"] = self.kwargs['pk']
        return context

    def get_success_url(self):
        recipe_object = self.object.recipe
        
        return reverse_lazy(
            'ledger:recipe_detail',
            kwargs={'pk': recipe_object.pk}
            )
