from django.contrib.auth.forms import SetPasswordForm, PasswordResetForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django_registration.forms import RegistrationForm

from quiz_auth.models import User


class QuizRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = User
    
    def __init__(self, *args, **kwargs):
        super(QuizRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Register"))


class QuizPasswordSetForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(QuizPasswordSetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Reset password"))
        
        
class QuizPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(QuizPasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit("submit", "Send email"))
