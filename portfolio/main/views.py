from typing import Any
from django.shortcuts import render
from django.contrib import messages

from .models import( UserProfile )


from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        

