
from django.urls import path
from api import views

urlpatterns = [
    path('', views.Home,name="home"),
    path('create-company', views.create_company,name="create-company"),
    path('company-list', views.company_list,name="company-list"),
    path('company-update/<int:pk>', views.company_update,name="company-update"),
    path('company-delete/<int:pk>', views.company_delete,name="company-delete"),
    path('create-user', views.create_user,name="create-user"),
    # path('notes/<int:pk>', views.get_single_note,name="notes"),
    
]







