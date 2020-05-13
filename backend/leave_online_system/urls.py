from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),    
    path('accounts/leave/', views.employee_form,name='employee_insert'),
    path('accounts/leave/<int:id>/', views.employee_form,name='leave_update'),
    path('accounts/leave/delete/<int:id>/', views.employee_delete, name='leave_delete'),
    path('accounts/list/', views.employee_list, name='employee_list')

    
]