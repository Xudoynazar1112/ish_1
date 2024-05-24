from django.urls import path
from .views import *

app_name = "users"
urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('employee/', EmployeeView.as_view(), name="employee"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profile-edit/', ProfileEditView.as_view(), name="profile_edit"),
]
