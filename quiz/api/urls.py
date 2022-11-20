from django.urls import path
from . import views

app_name = 'quiz'
urlpatterns = [
    path("", views.IndexView.as_view(), name="quiz-index"),
]