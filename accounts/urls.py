from django.urls import path, include
from accounts import views

app_name = 'accounts' 

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.signout, name='logout'),
]