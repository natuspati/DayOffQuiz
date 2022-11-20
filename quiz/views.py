from django.shortcuts import render
from django.views.generic import TemplateView
import logging
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.utils.decorators import method_decorator

from random import randint

logger = logging.getLogger(__name__)

decorators = [cache_page(5), vary_on_cookie]


@method_decorator(decorators, name='dispatch')
class IndexView(TemplateView):
    template_name = "quiz/index.html"
    
    def get(self, request, *args, **kwargs):
        logger.debug("Index page was accessed")
        return super(IndexView, self).get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["num"] = randint(0, 100)
        return context
