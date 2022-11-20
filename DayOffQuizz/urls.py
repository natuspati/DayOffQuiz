from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView

from django_registration.backends.activation.views import RegistrationView
from quiz_auth.forms import QuizRegistrationForm, QuizPasswordSetForm, QuizPasswordResetForm

import quiz_auth.views

from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("quiz.urls", namespace="quiz")),
    path("accounts/password_reset/",
         PasswordResetView.as_view(form_class=QuizPasswordResetForm,
                                   extra_email_context={"expiration_time": settings.PASSWORD_RESET_TIMEOUT}),
         name='password_reset'),
    path("accounts/reset/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(form_class=QuizPasswordSetForm),
         name='password_reset_confirm'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/register/",
         RegistrationView.as_view(form_class=QuizRegistrationForm),
         name="django_registration_register"),
    path("accounts/profile/", quiz_auth.views.ProfileView.as_view(),
         name="profile"),
    path('accounts/', include('django_registration.backends.activation.urls')),
    # path("api/v1/", include("quiz.api.urls")),
]
