
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('registration_view',views.registration_view,name='registration_view'),
    path('logout_view',views.logout_view,name='logout_view'),
    path('login_view',views.login_view,name='login_view'),
]
