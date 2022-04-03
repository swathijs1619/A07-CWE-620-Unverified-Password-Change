from django.urls import path
from . import views
urlpatterns = [
    path('', views.login_user, name='login'),
    path('home/', views.home , name ='home'),
    path('logout/', views.logout_view , name ='logout'),
    path('register/', views.register_view , name ='register'),
    path('edit-register/', views.edit_register_view , name ='edit_register'),
    path('change-password/', views.password_change , name ='password_change'),
    path('reset-password/', views.PasswordReset.as_view(),name ='password_reset'),
    path('reset-password-done/', views.PasswordResetDone.as_view(),name ='password_reset_done'),
    path('reset-password/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(),name ='password_reset_confirm'),
    path('reset-password-complete/', views.PasswordResetComplete.as_view(),name ='password_reset_complete'),
]
