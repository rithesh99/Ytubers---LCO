from django.urls import path
from . import views

urlpatterns = [
    path('login', views.signin, name="signin"),
    path('register', views.signup, name="signup"),
    path('logout', views.logout_user, name="logout_user"),
    path('dashboard', views.dashboard, name="dashboard")
]
