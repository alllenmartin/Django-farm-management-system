from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from authentication import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', user_views.signup, name='signup'),
    path('index/', user_views.home, name='index'),
    path('sent/', user_views.activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/',user_views.activate, name='activate'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'), name='password_reset' ),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'), name='password_reset_complete' ),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'), name='password_reset_done' ),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html'), name='password_reset_confirm' ),
    path('authentication/', include('authentication.urls')),
    path('app/', include('app.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)