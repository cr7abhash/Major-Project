from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic.base import View
# from django.views.generic import View
from .forms import MyRegistrationForm
from.models import ContactMessage



# Create your views here.
class login(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            login_status = "LOGGED IN as " + str(self.request.user.first_name)
        else:
            login_status = "NOT LOGGED IN"
        context = {
            "login_status": login_status,
        }
        return render(request, "users/login_page.html", context)

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            request.session["recommendation"] = []
            return HttpResponseRedirect("/products?login_success=True")
        else:
            print("Not Done !!")
            if self.request.user.is_authenticated:
                login_status = "LOGGED IN as " + str(self.request.user.first_name)
            else:
                login_status = "NOT LOGGED IN"
            
            context = {
                "invalid_login" : "True",
                "login_status": login_status,
            }
            return render(request, "users/login_page.html", context)

def logout(request):
    if request.user:
        auth.logout(request)
        request.session["recommendation"] = []
    return HttpResponseRedirect("/users?logout_success=True")


# New User Creation
def new_user_creation(request):
    if request.method == "POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/users?new_creation=True/")
        else:
            raise forms.ValidationError("Some Error during Data Entry !!")
    else:
        form = MyRegistrationForm()
        context = {
            "form" : form,
        }
        return render(request, "users/new_user_register.html", context)


def contact_us(request):
    if request.method == "POST":
        new_message = ContactMessage()
        new_message.full_name = request.POST.get("full_name")
        new_message.email = request.POST.get("email")
        new_message.address = request.POST.get("address")
        new_message.contact = request.POST.get("contact_no")
        new_message.message = request.POST.get("message")
        new_message.save()
        return HttpResponseRedirect("/products?message_sent=True")
    else:
        return render(request, "users/contact.html")


    
def about_us(request):
    return render(request, "users/about_us.html")
