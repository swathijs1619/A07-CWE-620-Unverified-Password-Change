import django
from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('sign-up/', views.signup, name="signup"),
    path('profile/', TemplateView.as_view(template_name="profile.html"), name="profile"),
    path('accounts/', include('django.contrib.auth.urls')),
]