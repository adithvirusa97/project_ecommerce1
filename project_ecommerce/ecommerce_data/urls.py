from django.urls import path
from .views import AdminHomepage,ViewUserData,ManageCategories,AddCategory,AddSubCategory
urlpatterns = [
    path('dashboard/', AdminHomepage.as_view(),name="dashboard"),
    path('all-users/', ViewUserData.as_view(),name="all_users"),
    path('manage-categories/', ManageCategories.as_view(),name="manage_categories"),
    path('add-category/', AddCategory.as_view(),name="addcategory"),
    path('add-sub-category/', AddSubCategory.as_view(),name="addsubcategory"),
    
]
