from django.shortcuts import render,redirect
from django.views import View
from authentication.models import NewUserModel
# Create your views here.
from django.contrib.auth import get_user_model
from .forms import CategoryForm,SubCategoryForm
from .models import Categories,SubCategories


class AdminHomepage(View):
    template='base.html'
    def get(self,request):
        return render(request,self.template,{})


class ViewUserData(View):
    template = 'table.html'
    def get(self,request):
        users = NewUserModel.objects.all()
        print(users)
        context = {}
        context["items"] =users
        return render(request,self.template,context)
    


class ManageCategories(View):
    template = 'category.html'
    def get(self,request):
        categories = Categories.objects.all()
        subcategories = SubCategories.objects.all()
        context ={}
        print(subcategories,"------------")
        context["categories"] = categories
        context["subcategories"] = subcategories
        return render(request,self.template,context)
    


class AddCategory(View):
    template = 'add_category.html'
    def get(self,request):
        form = CategoryForm()
        context = {}
        context["form"] = form
        print(form)
        return render(request,self.template,context)
    def post(self,request):
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("dashboard")

class AddSubCategory(View):
    template = 'add_category.html'
    def get(self,request):
        form = SubCategoryForm()
        context = {}
        context["form"] = form
        print(form)
        return render(request,self.template,context)
    def post(self,request):
        form = SubCategoryForm(request.POST)
        # print(form.cleaned_data,";;;;;;;;;;;;;;;;;;;")
        print(form.errors,"-----------------")
        print(form.errors)
        if form.is_valid():
            form.save()
        return redirect("dashboard")