from django import forms
from .models import Categories,SubCategories

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"

class SubCategoryForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Categories.objects.all(),to_field_name="category_name")
    class Meta:
        model = SubCategories
        fields = "__all__"

    