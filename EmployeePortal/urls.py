from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.getRoutes, name="routes"),
    path('employee/', views.getEmployeeBasicInfo, name="employee"),
    path('employee/<str:pk>/', views.getEmployeeBasicInfo, name="employee")

]