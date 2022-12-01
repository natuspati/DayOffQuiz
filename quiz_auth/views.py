from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.conf import settings

from django_registration.backends.activation.views import ActivationView

from .models import UserProfile


def create_default_profile_picture(first_name, last_name):
    import avinit
    
    svg_image = avinit.get_svg_avatar(
        first_name + " " + last_name,
        radius=15,
        colors=['#bf21f9']
    )
    
    with open(settings.MEDIA_ROOT + "profile_pictures/", "w") as f:
        f.write(svg_image)


class QuizActivationView(ActivationView):
    """
    The view creates its user profile with Gravatar.
    """
    
    def activate(self, *args, **kwargs):
        user = super(QuizActivationView, self).activate(*args, **kwargs)
        
        user_profile = UserProfile(user=user, bio="", date_of_birth=None)


@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = "quiz_auth/profile.html"


@method_decorator(login_required, name='dispatch')
class EditProfileView():
    pass

# TODO: Finish generating automatic avatars
# TODO: Connect custom activation view to URLconf
# TODO: Create UpdateView for editing profiles
# TODO: Connect edit profile view to URLConf
