from django.urls import path
from .views import login_view,Home,Register
urlpatterns = [
    path('register/', Register.as_view(),name="register"),
    path('login/', login_view,name="login"),
    path('home/', Home.as_view(),name="login"),
]
