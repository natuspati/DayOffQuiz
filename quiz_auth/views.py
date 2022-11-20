from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = "quiz_auth/profile.html"

