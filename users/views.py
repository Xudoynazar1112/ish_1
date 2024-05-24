from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreateForm, ProfileEditForm
from .models import User


def home(request):
    return render(request, "landing_page.html")


def about(request):
    return render(request, "users_templ/about.html")


def contact(request):
    return render(request, "users_templ/contact.html")


class EmployeeView(View):
    def get(self, request):
        employees = User.objects.all()
        context = {
            "employees": employees
        }
        return render(request, 'users_templ/employee.html', context)


class RegisterView(View):
    def get(self, request):
        create_form = UserCreateForm()
        context = {
            'form': create_form
        }
        return render(request, 'users_auth/register.html', context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST, files=request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request, 'users_auth/register.html', context)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'users_auth/login.html', {"login_form": login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect("users:home")   
        else:
            return render(request, 'users_auth/login.html', {"login_form": login_form})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "users_auth/profile.html", {"user": request.user})


class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        profile_edit_form = ProfileEditForm(instance=request.user)
        return render(request, "users_auth/profile_edit.html", {"form": profile_edit_form})

    def post(self, request):
        profile_edit_form = ProfileEditForm(instance=request.user, data=request.POST, files=request.FILES)
        if profile_edit_form.is_valid():
            profile_edit_form.save()
            return redirect("users:profile")

        return render(request, "users_auth/profile_edit.html", {"form": profile_edit_form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("users:home")