from django.shortcuts import render,redirect
from django.views import View
from authentication.models import NewUserModel

from django.contrib.auth import get_user_model
from .forms import CategoryForm,SubCategoryForm,StocksForm
from .models import Categories,SubCategories,Products
from django.http import HttpResponse,JsonResponse


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
        form = CategoryForm(request.POST,request.FILES)
        
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
        form = SubCategoryForm(request.POST,request.FILES)
        # print(form.cleaned_data,";;;;;;;;;;;;;;;;;;;")
        print(form.errors,"-----------------")
        print(form.errors)
        if form.is_valid():
            form.save()
        return redirect("dashboard")
    
class ManageStocks(View):
    template = 'stocks.html'
    def get(self,request):
        products = Products.objects.all()
        context = {}
        context["products"] = products
        return render(request,self.template,context)
    

class AddStock(View):
    template = 'add_category.html'
    def get(self,request):
        form = StocksForm()
        context = {}
        context["form"] = form
        print(form)
        return render(request,self.template,context)
    def post(self,request):
        form = StocksForm(request.POST,request.FILES)
        context = {}
        context["form"] = form
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        else:
            return render(request,self.template,context)
        


class ModifyStocks(View):
    template = 'add_category.html'
    def get(self,request,id):
        instance = Products.objects.get(id=id)
        form = StocksForm(instance=instance)
        context = {}
        context["form"] = form
        print(form)
        return render(request,self.template,context)
    def post(self,request,id):
        instance = Products.objects.get(id=id)
        form = StocksForm(request.POST,request.FILES,instance=instance)
        context = {}
        context["form"] = form
        print(form.errors,"----------------")
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        else:
            return render(request,self.template,context)
class DeleteStocks(View):
    def get(self,request,id):
        instance = Products.objects.get(id=id)
     
        instance.delete()
        return redirect('manage_stocks')
    
class Homepage(View):
    template = 'homepage.html'
    def get(self,request):
        context={}
        categories = Categories.objects.all()
        products = Products.objects.all()
        context["categories"] = categories
        context["products"] = products
        return render(request,self.template,context)
    


class CategoryDelete(View):
    def get(self,request,id):
        print(id,"---------------",type(id))
        
        instance = Categories.objects.get(id=id)
        instance.delete()
        return redirect('manage_categories')
class SubCategoryDelete(View):
    def get(self,request,id):
        instance = SubCategories.objects.get(id=id)
     
        instance.delete()
        return redirect('manage_categories')
    

class CategoryEdit(View):
    template = 'add_category.html'
    def get(self,request,id):
        instance = Categories.objects.get(id=id)
        form = CategoryForm(instance=instance)
        context = {}
        context["form"] = form
        print(form)
        return render(request,self.template,context)
    def post(self,request,id):
        instance = Categories.objects.get(id=id)
        form = CategoryForm(request.POST,request.FILES,instance=instance)
        context = {}
        context["form"] = form
        print(form.errors,"----------------")
        if form.is_valid():
            form.save()
            return redirect("manage_categories")
        else:
            return render(request,self.template,context)
class SubCategoryEdit(View):
    template = 'add_category.html'
    def get(self,request,id):
        instance = SubCategories.objects.get(id=id)
        form = SubCategoryForm(instance=instance)
        context = {}
        context["form"] = form
        print(form)
        return render(request,self.template,context)
    def post(self,request,id):
        instance = SubCategories.objects.get(id=id)
        form = SubCategoryForm(request.POST,request.FILES,instance=instance)
        context = {}
        context["form"] = form
        print(form.errors,"----------------")
        if form.is_valid():
            form.save()
            return redirect("manage_categories")
        else:
            return render(request,self.template,context)