from django.urls import path
from .import views

urlpatterns=[
	path('',views.login_view,name='login'),
	path('/profile',views.profile,name='profile'),
	path('/about',views.about,name='about'),
	path("logut/",views.logout_view,name="logout"),
	]