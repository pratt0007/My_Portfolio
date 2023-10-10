from typing import Any
from django.shortcuts import render
from django.contrib import messages

from .models import( UserProfile, portfolio , certificate , contactprofile)

from .forms import contactform

from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    

class PortfolioDetailView(generic.DetailView):
	model = portfolio
	template_name = "main/portfolio-detail.html"
class PortfolioView(generic.ListView):
	model = portfolio
	template_name = "main/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)

class ContactView(generic.FormView):
	template_name = "main/contact.html"
	form_class = contactform
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)

