from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # Use built-in LogoutView via GET or POST depending on Django version/config, 
    # but for simplicity in older styles or simple apps, often GET is used via link.
    # Django 5+ requires POST for logout by default, but we can wrap it or use a form in template.
    # For now, standard view.
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
