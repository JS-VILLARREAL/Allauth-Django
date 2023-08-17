from django.urls import path
from .views import home, profile

urlpatterns = [
    path('', home, name='home'),
    path('account/profile/', profile, name='profile'),
]
