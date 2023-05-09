
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.views import View
from django.http import HttpResponse
from .forms import RegistrationForm



# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')



class Register(View):
    template = 'register.html'
    def get(self,request):
        print("entereeddd get")
        form = RegistrationForm()
        print(form,"----------------")
        context ={}
        context["form"]=form
        return render(request,self.template,context)
    def post(self,request):
        print("hiiii")
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("validdddd")
            form.save()
        else:
            print(form.errors,"-----------------------")

        return redirect("dashboard")



class Home(View):
    def get(self,request,*args,**kwargs):
        return HttpResponse("hiiii")
