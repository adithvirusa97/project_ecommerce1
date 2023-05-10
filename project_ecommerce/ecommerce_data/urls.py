from django.urls import path
from .views import AdminHomepage,ViewUserData,ManageCategories,AddCategory,AddSubCategory,ManageStocks,AddStock,ModifyStocks,DeleteStocks,Homepage,CategoryEdit,SubCategoryEdit,CategoryDelete,SubCategoryDelete
urlpatterns = [
    path('dashboard/', AdminHomepage.as_view(),name="dashboard"),
    path('all-users/', ViewUserData.as_view(),name="all_users"),
    path('manage-categories/', ManageCategories.as_view(),name="manage_categories"),
    path('add-category/', AddCategory.as_view(),name="addcategory"),
    path('add-sub-category/', AddSubCategory.as_view(),name="addsubcategory"),
    path('manage-stocks/', ManageStocks.as_view(),name="manage_stocks"),
    path('add-stocks/', AddStock.as_view(),name="add_stock"),
    path('edit-stocks/<int:id>', ModifyStocks.as_view(),name="edit_stocks"),
    path('delete-stocks/<int:id>', DeleteStocks.as_view(),name="delete_stocks"),
    path('', Homepage.as_view(),name="homepage"),
    path("edit-category/<int:id>",CategoryEdit.as_view(),name="edit_category"),
    path("edit-subcategory/<int:id>",SubCategoryEdit.as_view(),name="edit_subcategory"),
    path("delete-category/<int:id>",CategoryDelete.as_view(),name="delete_category"),
    path("delete-subcategory/<int:id>",SubCategoryDelete.as_view(),name="delete_subcategory"),
    
]
