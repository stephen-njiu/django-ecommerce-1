from django.urls import path 
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from . import views 
from .forms import LoginForm
from .views import logout_view

app_name = 'core' 

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('logout/', logout_view, name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login')
]