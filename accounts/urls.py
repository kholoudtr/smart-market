from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('home/',views.home,name='home'),  
    path('',views.signup,name='signup'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('settings/change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html',success_url='/settings/change_password_done/'), name='change_password' ),
    path('settings/change_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'), name='change_password_done'),
        # إعادة تعيين كلمة المرور

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
 
    
]
