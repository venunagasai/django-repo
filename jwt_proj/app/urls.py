from django.urls import path
from .views import login_page, profile_page, ProtectedDataView

urlpatterns = [
    path('login/', login_page, name='login'),
    path('profile/', profile_page, name='profile'),
    path('api/profile-data/', ProtectedDataView.as_view(), name='profile-data'),
]
